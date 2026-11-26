import os 

import pandas as pd 
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

CSV_PATH = "data/raw/bigmart_sales.csv"   
TABLE_NAME = "bigmart_sales"

def extract(path):
    df = pd.read_csv(path)
    print(f"Extracted {len(df)} rows")
    return df

def transform(df):
    df = df.copy()

    fit_map = {"LF": "Low Fat", "low fat": "Low Fat", "reg": "Regular"}
    df["Item_Fat_Content"] = df["Item_Fat_Content"].replace(fit_map)

    df["Item_Weight"] = df["Item_Weight"].fillna(df["Item_Weight"].median())
    df["Outlet_Size"] = df["Outlet_Size"].fillna("Unknown")

    df = df.drop_duplicates()

    print(f"Transformed data: {len(df)} rows") 
    return df

def get_engine():
    load_dotenv()
    url = URL.create(
        "postgresql+psycopg2",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME"),
    )
    return create_engine(url)

def load(df, engine):
    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into table '{TABLE_NAME}'")

def main():
    raw = extract(CSV_PATH)
    clean = transform(raw)
    engine = get_engine()
    load(clean, engine)


if __name__ == "__main__":
    main()

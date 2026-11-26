# BigMart Sales ETL: CSV to PostgreSQL

A Python ETL pipeline that extracts a messy sales CSV, cleans it with pandas, loads it into PostgreSQL with SQLAlchemy, and verifies the load with SQL checks.

## Dataset
BigMart Sales data (8,523 rows, 12 columns) with product, outlet and sales details.

## Tech Stack
Python, pandas, PostgreSQL, SQLAlchemy, Git

## Pipeline
1. **Extract**: read the raw CSV from `data/dat/raw/`
2. **Transform**: clean the data with pandas
3. **Load**: write the cleaned data into a PostgreSQL table (`bigmart_sales`)
4. **Verify**: run SQL queries to confirm row counts, nulls and totals

## Data Cleaning
- Standardized `Item_Fat_Content`: `LF` / `low fat` became `Low Fat`, and `reg` became `Regular`
- Filled missing `Item_Weight` values (1,463) with the median weight
- Filled missing `Outlet_Size` values (2,410) with `Unknown`, because three whole outlets had no size recorded
- Checked for and removed duplicate rows (none found)

## Project Structure
```
sales-etl-postgreSQL/
├── data/data/raw/          # original CSV
├── sql/checks.sql     # verification queries
├── explore.ipynb      # data exploration and cleaning experiments
├── etl.py             # the pipeline script
├── requirements.txt
└── README.md
```

## How to Run
1. Clone the repo and create a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Install PostgreSQL and create a database named `sales_db`.
3. Create a `.env` file in the project root:
   ```
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=sales_db
   ```
4. Run the pipeline:
   ```
   python etl.py
   ```

## Verification
The queries in `sql/checks.sql` check:
- Total row count (8,523)
- No null values remain
- Fat content has only 2 categories
- Total sales matches pandas
- Sales summary by outlet type

## Re-runnable
The script is idempotent: the table is rebuilt on each run, so re-running it never creates duplicate rows.

## What I Learned
- How an ETL pipeline is structured: separate `extract`, `transform` and `load` functions, with credentials kept in a `.env` file instead of in the code.
- Why re-running a pipeline can create duplicate rows, and how `if_exists="replace"` makes the script idempotent. I also learned what an incremental load is and would use one for data that keeps arriving.
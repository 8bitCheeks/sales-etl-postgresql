-- 1. Row count (expect 8523)
SELECT COUNT(*) AS total_rows
FROM bigmart_sales;

-- 2. No nulls left (expect 0 and 0)
SELECT
    COUNT(*) - COUNT(Item_Weight) AS null_weights,
    COUNT(*) - COUNT(Outlet_Size) AS null_outlet_sizes
FROM bigmart_sales;

-- 3. Clean categories (expect Low Fat 5517, Regular 3006)
SELECT Item_Fat_Content, COUNT(*) AS items
FROM bigmart_sales
GROUP BY Item_Fat_Content;

-- 4. Total sales (compare with pandas)
SELECT ROUND(SUM(Item_Outlet_Sales)) AS total_sales
FROM bigmart_sales;

-- 5. Sales by outlet type
SELECT Outlet_Type,
       COUNT(*) AS rows,
       ROUND(SUM(Item_Outlet_Sales)) AS total_sales
FROM bigmart_sales
GROUP BY Outlet_Type
ORDER BY total_sales DESC;

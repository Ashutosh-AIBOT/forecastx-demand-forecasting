-- ============================================================
-- Product Demand Forecasting – SQL Analysis
-- Database: SQLite (used via Python in the notebook)
-- ============================================================


-- 1. Preview the raw table
SELECT *
FROM demand
LIMIT 10;


-- 2. Count total records
SELECT COUNT(*) AS total_rows
FROM demand;


-- 3. Check for NULL values per column
SELECT
    SUM(CASE WHEN "Product_Code"   IS NULL THEN 1 ELSE 0 END) AS null_product,
    SUM(CASE WHEN "Warehouse"      IS NULL THEN 1 ELSE 0 END) AS null_warehouse,
    SUM(CASE WHEN "Product_Category" IS NULL THEN 1 ELSE 0 END) AS null_category,
    SUM(CASE WHEN "Date"           IS NULL THEN 1 ELSE 0 END) AS null_date,
    SUM(CASE WHEN "Order_Demand"   IS NULL THEN 1 ELSE 0 END) AS null_demand
FROM demand;


-- 4. Distinct warehouses
SELECT DISTINCT Warehouse
FROM demand
ORDER BY Warehouse;


-- 5. Distinct product categories
SELECT DISTINCT Product_Category
FROM demand
ORDER BY Product_Category;


-- 6. Total demand per warehouse
SELECT
    Warehouse,
    SUM(Order_Demand) AS total_demand,
    COUNT(*)          AS order_count
FROM demand
GROUP BY Warehouse
ORDER BY total_demand DESC;


-- 7. Total demand per product category
SELECT
    Product_Category,
    SUM(Order_Demand)  AS total_demand,
    COUNT(*)           AS order_count,
    AVG(Order_Demand)  AS avg_demand
FROM demand
GROUP BY Product_Category
ORDER BY total_demand DESC;


-- 8. Top 10 products by total demand
SELECT
    Product_Code,
    SUM(Order_Demand) AS total_demand
FROM demand
GROUP BY Product_Code
ORDER BY total_demand DESC
LIMIT 10;


-- 9. Monthly demand trend (aggregated)
SELECT
    strftime('%Y-%m', Date) AS month,
    SUM(Order_Demand)       AS monthly_demand
FROM demand
WHERE Date IS NOT NULL
GROUP BY month
ORDER BY month;


-- 10. Yearly demand summary
SELECT
    strftime('%Y', Date) AS year,
    SUM(Order_Demand)    AS yearly_demand,
    COUNT(*)             AS order_count
FROM demand
WHERE Date IS NOT NULL
GROUP BY year
ORDER BY year;


-- 11. Demand breakdown: warehouse × category
SELECT
    Warehouse,
    Product_Category,
    SUM(Order_Demand) AS total_demand
FROM demand
GROUP BY Warehouse, Product_Category
ORDER BY total_demand DESC;


-- 12. Average demand per product per warehouse
SELECT
    Product_Code,
    Warehouse,
    AVG(Order_Demand) AS avg_demand,
    MAX(Order_Demand) AS peak_demand
FROM demand
GROUP BY Product_Code, Warehouse
ORDER BY avg_demand DESC
LIMIT 20;


-- 13. Orders with unusually high demand (> 99th percentile proxy)
SELECT *
FROM demand
WHERE Order_Demand > (
    SELECT AVG(Order_Demand) + 3 * (
        SELECT AVG((Order_Demand - sub.avg_val) * (Order_Demand - sub.avg_val))
        FROM demand, (SELECT AVG(Order_Demand) AS avg_val FROM demand) sub
    )
    FROM demand
)
ORDER BY Order_Demand DESC
LIMIT 20;


-- 14. Products appearing in all warehouses
SELECT Product_Code
FROM demand
GROUP BY Product_Code
HAVING COUNT(DISTINCT Warehouse) = (SELECT COUNT(DISTINCT Warehouse) FROM demand);


-- 15. Recent 90 days demand (relative to max date in dataset)
SELECT *
FROM demand
WHERE Date >= (
    SELECT DATE(MAX(Date), '-90 days') FROM demand
)
ORDER BY Date DESC;

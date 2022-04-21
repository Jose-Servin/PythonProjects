REPORT_ONE_QUERY = """
SELECT region, 
	AVG(profit)::NUMERIC::money AS Avg_Profit  
FROM super_store 
GROUP BY region
ORDER BY AVG(profit) DESC
"""

REPORT_TWO_QUERY = """
SELECT state, 
COUNT (DISTINCT order_id) as Volume
FROM super_store
GROUP BY state
ORDER BY Volume DESC
"""

REPORT_THREE_SHEET_ONE_QUERY = """
SELECT region,
	state,
	AVG(profit)::NUMERIC::money AS Avg_Profit
FROM super_store 
GROUP BY region, state
ORDER BY AVG(profit) DESC
"""

REPORT_THREE_SHEET_TWO_QUERY = """
SELECT * FROM (
	SELECT
		*,
		RANK() OVER ( ORDER BY Avg_Profit DESC) AS rank
		FROM
	(

		SELECT
			region,
			city,
			state,
			AVG(profit)::NUMERIC::money AS Avg_Profit
		FROM super_store
		GROUP BY region, city, state
		ORDER BY Avg_Profit DESC

	) AS rank_table
) AS final_data

WHERE rank <= 60
"""

REPORT_FOUR_SHEET_ONE_QUERY = """
SELECT 
	state, 
	category,
	sub_category,
	AVG(profit)::NUMERIC::money AS Avg_Profit
FROM super_store
GROUP BY state, 
	category,
	sub_category
ORDER BY AVG(profit)::NUMERIC::money DESC
"""
REPORT_FOUR_SHEET_TWO_QUERY = """
SELECT	
	category,
	sub_category,
	SUM(profit)::NUMERIC::money as Total_Profit
FROM super_store
GROUP BY category,
	sub_category
ORDER BY
	SUM(profit)::NUMERIC::money DESC
"""
REPORT_FOUR_SHEET_THREE_QUERY = """
WITH MASTER_DATA AS (
	SELECT 
		state,
		SUM(profit) as profit
	FROM super_store
	WHERE 
		category = 'Technology' AND
		sub_category = 'Copiers'
	GROUP BY state
)
SELECT state, 
	SUM(profit) OVER (ORDER BY state)::NUMERIC::money as Running_Profit_Sum
FROM MASTER_DATA
"""

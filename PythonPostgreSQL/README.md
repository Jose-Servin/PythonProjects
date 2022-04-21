# Project Overview 

## Dataset used 
The dataset used for this project comes from 
[Kaggle](https://www.kaggle.com). Specifically, this 
dataset is called the <strong> Superstore Dataset. </strong> More information can be found 
[here](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download). There are lots of great 
datasets available to replicate this project. Your main focus should be to find an interesting dataset that is 
relatively clean in order to minimize the data cleaning process. One note, the Superstore Dataset did contain some 
special characters, specifically in the customer name column. This will cause an issue when importing data in Kaggle 
therefore a quick review of the data is recommended. 



## Creating SQL Tables
For this project I am using Postgres syntax and PgAdmin as my tool to interact with my Postgres database. When 
creating the sql tables I recommend you look at the dataset and think "what datatype best represents this column?". 
For some instances there can be more than one answer such as `SMALLINT` or `INT` but ultimately there will be one 
answer that best fits. The table creation syntax is provided below. 
```postgresql
CREATE TABLE IF NOT EXISTS super_store (
	row_id serial PRIMARY KEY,
	order_id varchar(255) NOT NULL, 
	order_date DATE,
	ship_date DATE,
	ship_mode varchar(255),
	customer_id varchar(255) NOT NULL,
	customer_name varchar(255) NOT NULL,
	segment varchar(255),
	country varchar(255),
	city varchar(255),
	state varchar(255),
	postal_code varchar(255),
	region varchar(255),
	product_id varchar(255),
	category varchar(255),
	sub_category varchar(255),
	sales float(8),
	quantity integer,
	discount float(8),
	profit float(8)
)
```
<mark> One important note: </mark>  <br>

As stated in the Dataset used section, there were some instances of special characters that went against UTF-8 standards. 
Therefor, the column `product name` was deleted from the csv file for two main reasons:
1. The column contained numerous invalid characters which would require extensive regex/text cleaning. 
2. It is my personal opinion this column offered no value therefore I chose to delete it from consideration. 
<br>

If you wish to clean the non UTF-8 characters this might 
[help](https://stackoverflow.com/questions/12999651/how-to-remove-non-utf-8-characters-from-text-file) you. 

## Reports 

### Report One: What region is most profitable? 
Looking at this data, the simplest aggregating we can do is to group by region and examine the avg of profit. This 
will show us what region is most profitable allowing us to dive deeper into states, cities and finally customers. It 
is the goal of every business to identify what customer maximizes profit.
```postgresql
SELECT region, 
	AVG(profit)::NUMERIC::money AS Avg_Profit  
FROM super_store 
GROUP BY region
ORDER BY AVG(profit) DESC; 
```
Here we are selecting region and taking the avg of profit. Because we are aggregating we must `GROUP BY` region and 
cast the `Avg_Profit` as `NUMERIC` and then `money`. This double casting is due to our profit column being a 
double-precision datatype. Postgres documentation over converting to money can be found 
[here](https://www.postgresql.org/docs/current/datatype-money.html). 


### Report Two: In what State do you sell the most? based on Volume 

To see where you sell the most we can use a simple `count` aggregate function.
```postgresql
SELECT state, 
COUNT (DISTINCT order_id) as Volume
FROM super_store
GROUP BY state
ORDER BY Volume DESC;
```
If you would like to verify this information by getting a sum of all unique order, we must recognize that `order_id`'s
are not unique values therefore duplicate rows exist. To eliminate duplicates and only count unique orders we can use a 
combination of `COUNT` and `DISTINCT`:
```postgresql
SELECT 	
	COUNT(*) 
FROM (SELECT DISTINCT order_id FROM super_store) AS unique_data;
```
From this query we see there are 5009 unique order_id's which matches the value returned by the simple aggregate 
function. 

### Report Three
Report three will provide two key pieces of information.
1. What is our most profitable State? 
```postgresql
SELECT region,
	state,
	AVG(profit)::NUMERIC::money AS Avg_Profit
FROM super_store 
GROUP BY region, state
ORDER BY AVG(profit) DESC;
```
2. What are our top 10% most profitable City - State combinations?

* First we must determine how many unique City - State combinations exist:
```postgresql
SELECT COUNT(*) FROM (SELECT 
DISTINCT city, state FROM super_store)
AS unique_city_states;
```

* Next we limit the rank to 10% of this value:

```postgresql
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

WHERE rank <= 60;
```
### Report 4
Report four will show us what product is most profitable in each state. 
```postgresql
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
```
Now let's see what's the sum of profit for the category/sub-category groups:
```postgresql
SELECT	
	category,
	sub_category,
	SUM(profit)::NUMERIC::money as Total_Profit
FROM super_store
GROUP BY category,
	sub_category
ORDER BY
	SUM(profit)::NUMERIC::money DESC
```
Lastly, let's see a running sum of profit for the top category/sub_category group `Technology / Copiers`:
```postgresql
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
FROM MASTER_DATA;
```
## Project Routes
Now that we've confirmed that both our queries run and that the data looks correct we will move on to the Python 
part of the project. Here, there are two options we can take:
1. We save the reports as `csv`'s or `.xlsx` files in our local machine and then use Python to automate the actions of 
   grabbing those reports and emailing them out.
2. We connect to the database and run the queries using Python and then save those reports in an email as attachments 
   and send out a secure email using Gmail Developer Tools/API. 

There are pros and cons to both options but for this project I am going to select option two. I am doing this in 
order to challenge myself to use the Google API tools and to create a more structured automation program using Python. 

## Project Structure 

For this project, the root directory will be `PythonPostgreSQL` with two subdirectories. The first subdirectory will 
be `modules` which will contain a `.py` file with all the methods used for this project. This means, we will run 
this project by running `python3 <path to .py file>`. The second module is called `tests`, here we will test all 
the methods used in the `super_store.py` file.

### Why this structure?
For this project, we are building a python script. A python script is a collection of commands in a file designed to 
be executed like a program. So, our reporting will be generated by the `super_store.py` file which will contain all 
the functions needed to:
1. Connect to database
2. Query database
3. Save results
4. Email results 

By having all of this in one file, we simplify the implementation of our project. Later on, I will work on creating 
more structured projects with OOP principles and directory / subdirectory structure. Note that I've added the `test` 
directory in order to have some sort of code coverage in this project and to practice my python testing skills. 

## Python Functions
In this section, I'll provide a brief summary of the functions we need and attempt to provide a project flow. <br>

Process Flow:
1. Connect to database 
2. Query database
3. Build newMail object using Gmail Developers Tools
4. Save query results as attachments 
5. send email to personal gmail from test gmail 

## Project Development
To start, I tested the connection to database and querying part using a simple script.
```python
import psycopg2
from super_store_functions import create_connection
from constants import REPORT_ONE_QUERY
import pandas as pd


def script_function():
    conn = create_connection()

    # Define Python cursor class object
    cur = conn.cursor()

    # Query database
    cur.execute(REPORT_ONE_QUERY)

    # Save query results
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()

    conn.close()


if __name__ == "__main__":
    script_function()
```
After confirming this works, I'll move on storing the results in a DataFrame. 
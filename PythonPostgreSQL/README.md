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
Looking at this data, the simplest aggregating we can do is to group by region and examine the sum of profit. This 
will show us what region is most profitable allowing us to dive deeper into states, cities and finally customers. It 
is the goal of every business to identify what customer maximizes profit.
```postgresql
SELECT region, 
	SUM(profit)::NUMERIC::money AS sum_of_profit  
FROM super_store 
GROUP BY region
ORDER BY SUM(profit) DESC
```
Here we are selecting region and taking the sum of profit. Because we are aggregating we must `GROUP BY` region and 
cast the `sum_of_profit` as `NUMERIC` and then `money`. This double casting is due to our profit column being a 
double-precision datatype. Postgres documentation over converting to money can be found 
[here](https://www.postgresql.org/docs/current/datatype-money.html). 

## Report two
Report two will provide two key pieces of information.
1. What is our top 3 states in the West that are most profitable. 
2. From the top 3 states, what is our top 2 cities that are most profitable. 

Such that in the end we will have our top 6 states from our top 3 cities based on profitability. 

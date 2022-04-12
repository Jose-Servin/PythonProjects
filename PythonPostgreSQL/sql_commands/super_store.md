# Super Store SQL Commands

## Dataset used 

## Data cleaning issues 


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
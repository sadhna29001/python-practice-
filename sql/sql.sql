-- OPERATORS
-- 1) OPERATOR: An Operator is a symbol that tells the compiler to perform specific mathematical,
--    relational or logical operation to produce a desired result.
-- 2) OPERAND: An operand is an object which is operated upon by any operator to produce a result.
-- 3) EXPRESSION: An expression is a combination of one or more operators and operands which together
-- 				  produce a meaningful result.
-- 4) Example- 2 + 3 = 5. Here, '+' is an operator and '2'&'3' are operands and '5' is the result

-- 5) There are 4 types of Operators:-
--    a) Arithmetic Operators(+,-,*,/,%)
--    b) Comparison Operators(=,>,<,>=,<=,<>/ or !=)
--    c) Bitwise Operators(&,|,^)
--    d) Logical Operators(AND, ALL, ANY, BETWEEN, EXISTS, IN, LIKE, NOT, OR, SOME)

-- A) ARITHMETIC OPERATORS
-- They are used for mathematical calculations
-- There are 5 types:
-- a) Addition{+}: Gives sum of operands. Ex- 6+7=13
-- USAGE
SELECT 6+7;
-- b) Subtraction{-}: Gives difference of operands. Ex- 4-2=2
-- USAGE
SELECT 4-2;

-- c) Multiplication{+}: Gives product of operands. Ex- 6*4=24
-- USAGE
SELECT 6*4;

-- d) Division{/}: Gives quotient of 5 divided by 3. Ex- 7/4=1.75
-- USAGE
SELECT 7/4;

-- e) Modulo{%}: Gives remainder of 5 divided by 3. Ex- 3%2=1
-- USAGE
SELECT 3%2;


-- B) COMPARISON OPERATORS
--    They are used to compare the operands and give result in True or False
-- There are 6 types:
-- a) Equals To{=}: Gives true if operands are real. Ex- 7=7
-- USAGE
SELECT 7=7;

-- b) Greater Than{>}: Gives true if left operand is greater. Ex- 8>3
-- USAGE
SELECT 8>3;

-- c) Less Than{<}: Gives true if left operand is lesser. Ex- 1<5
-- USAGE
SELECT 1<5;

-- d) Greater Than or Equals To{>=}: Gives true if left operand is greater or equal. Ex- 8>=8
-- USAGE
SELECT 8>=8;

-- e) Less Than or Equals To{<=}: Gives true if left operand is lesser or equal. Ex- 4<=6
-- USAGE
SELECT 4<=6;

-- e)Not Eqauls To{<> or !=}: Gives true if operands are unequal. Ex- 3<>6
-- USAGE
SELECT 3<>6;

-- C) BITWISE OPERATORS
--    They compare each bit of the first operand to the correponding bit of the second operand and produce a final result.
--    Basically, Operands are converted to binary and than operated on by operators and the binary result is converted to human readable form.
-- They are of 3 types:
-- a) Bitwise AND{&}: Result contains AND operated bits. Ex- 56&47=43
-- USAGE
SELECT 56 & 47;

-- b) Bitwise OR{|}: Result contains OR operated bits. Ex- 59|47=63
-- USAGE
SELECT 59 | 47;

-- c) Bitwise XOR{^}: Result contains XOR operated bits. Ex- 59^47=20
-- USAGE
SELECT 59 ^ 47;

-- D) LOGICAL OPERATORS
--    They connect two or more boolean expressions such that the result of the compound expression depends on the
--    results of the original expressions and on the meaning of the operator. Results are in True and False.
-- Commonly Used Types:
-- a) AND: Gives True if all conditions separated by AND are True. Ex- 4!=6 AND 12>6
-- USAGE
SELECT 4!=6 AND 12>6;

-- b) OR: Gives True if any of the conditions separated by OR is True. Ex- 5>4 AND 10=6
-- USAGE
SELECT 5>4 AND 10=6;

-- c) NOT: Gives true if condition is False, false if condition is True. Ex- NOT 3<5
-- USAGE
SELECT NOT 3<5;

-- d) LIKE: Gives true if operand matches a pattern. Ex- 'Hello' LIKE '%o'
-- USAGE
SELECT 'Hello' LIKE '%o';

-- e) BETWEEN: Gives true if operand is within the range of comparisons. Ex- 5 BETWEEN 1 AND 10
-- USAGE
SELECT 5 BETWEEN 1 AND 10;

# --------------------------------------------QUESTIONS---------------------------------------------
/*
Arithmetic Operators:
1) How would you calculate the remainder when dividing an employee's ID by 5
2) Write a query to round an employee's salary to the nearest hundred.
3) Write a query to subtract the average price from the price of each product and display the result as 
   price_difference.
   
Comparison Operators:
1)  How do you select all employees whose salary is greater than $50,000
2) How do you select customers whose names start with 'A'
3) Write a query to retrieve all orders where the order amount is less than or equal to 10000.

Bitwise Operators:
1) Explain the bitwise AND (&) operator with an example.
2) Explain the bitwise OR (|) operator with an example.
3) Explain the bitwise XOR (^) operator with an example.

Logical Operators:
1) How do you select all employees who are either in the 'Sales' department OR have a salary greater than 50000
2) How do you select products that have a price between 10 and 20
3) How do you select customers who are not from 'New York'
*/
# ANSWERS
-- Arithmetic Operators:
-- 1)
SELECT employee_id, employee_id % 5 AS remainder FROM employees;
-- 2)
SELECT employee_id, ROUND(salary, -2) AS rounded_salary FROM employees;
-- 3)
SELECT pid, pname, price, 
(price - (SELECT AVG(price) FROM products)) AS price_difference 
FROM products;

-- Comparison Operators:
-- 1)
SELECT * FROM employees WHERE salary > 50000;
-- 2)
SELECT * FROM customers WHERE name LIKE 'A%';
-- 3) 
SELECT * 
FROM orders 
WHERE amt <= 10000;

-- Bitwise Operators:
-- 1) The bitwise AND (&) operator performs a binary AND operation on each pair of corresponding bits in the operands.
--    For example, 5 & 3 in binary is 0101 & 0011 which results in 0001, which is the decimal value 1.
-- 2) The bitwise OR (|) operator performs a binary OR operation on each pair of corresponding bits in the operands.
--    For example, 5 | 3 in binary is 0101 | 0011 which results in 0111, which is the decimal value 7.
-- 3) The bitwise XOR (^) operator performs a binary XOR operation on each pair of corresponding bits in the operands.
--    For example, 5 ^ 3 in binary is 0101 ^ 0011 which results in 0110, which is the decimal value 6.

-- Logical Operators:
-- 1)
SELECT * FROM employees WHERE department = 'Sales' OR salary > 50000;
-- 2)
SELECT * FROM products WHERE price >= 10 AND price <= 20;




#----------------- Introduction to sql-------------------------
/* 
DATATYPES 
 NUMERIC DATA TYPE 
1) INT(size)
2) BIGINT(size)
3) FLOAT(size , d) here d is no.of digits after the decimal points.
4) DOUBLE
5) DECIMAL

 DATE AND TIME DATATYPE
1) DATE: FORMAT : YYYY-MM-DD
2) DATETIME: FORMAT : YYYY-MM-DD hh:mm:ss
3) TIME :FORMAT : hh:mm:ss
4) YEAR : FORMAT : 1901 to 2155, and 0000.

 STRING DATATYPES
1) CHAR 
2) VARCHAR
3) TEXT
 */
 
 -- Create database
create database urban_company;

use urban_comapny;

-- Products - pid, pname, price, stock, location (Mumbai or Delhi)
create table products
(
	pid int(3) primary key,
    pname varchar(50) not null,
    price int(10) not null,
    stock int(5),
    location varchar(30) check(location in ('Mumbai','Delhi'))
);

-- Customer - cid, cname, age, addr
create table customer
(
	cid int(3) primary key,
    cname varchar(30) not null,
    age int(3),
    addr varchar(50)
);

-- Orders - oid, cid, pid, amt
create table orders
(
	oid int(3) primary key,
    cid int(3),
    pid int(3),
    amt int(10) not null,
    foreign key(cid) references customer(cid),
    foreign key(pid) references products(pid)
);


-- Payment - pay_id, oid,amount, mode(upi, cerdit, debit), status
create table payment
(
	pay_id int(3) primary key,
    oid int(3),
    amount int(10) not null,
    mode varchar(30) check(mode in('upi','credit','debit')),
    status varchar(30),
    foreign key(oid) references orders(oid)
);


-- to delete table we use drop 
drop table products ;

-- to drop whole database we use command
drop database amazon;

-- from alter command we can add and modify the tables 
-- to add column in a table 
alter table customer
add phone varchar(10);

-- to delete a column 
alter table customer
drop column phone;

-- to rename column 
alter table orders
rename column amt to amount ;

-- to modify datatype or add conditions
alter table products
modify column price varchar(10) ;

alter table products
modify column location varchar(30) check(location in ('Mumbai','Delhi' , 'chennai')) ;

-- TURNCATE
-- The TRUNCATE TABLE command deletes the data inside a table, but not the table itself.
truncate table products ;

/*
CONSTRAINTS
NOT NULL - Ensures that a column cannot have a NULL value
UNIQUE - Ensures that all values in a column are different
PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
FOREIGN KEY - Prevents actions that would destroy links between tables
CHECK - Ensures that the values in a column satisfies a specific condition
DEFAULT - Sets a default value for a column if no value is specified
*/

-- implementation
alter table customer
modify column age int(2) not null;

alter table customer
modify column phone varchar(10) unique ;

alter table payment
modify column status varchar(30) check( status in ('pending' , 'cancelled' , 'completed'));

alter table products
modify column location varchar(30) default 'Mumbai' check(location in ('Mumbai','Delhi' , 'chennai')) ;

/*
DML (Data Manipulation Language) commands  focus on adding, updating, and deleting data within database tables.

INSERT: Adds new rows to a table. 
UPDATE:  This command can update one or multiple rows at once.
DELETE: it can delete one or multiple rows depending on the conditions provided.
 */

-- implementation
#Inserting values into products table
insert into products values(1,'HP Laptop',50000,15,'Mumbai');
insert into products values(2,'Realme Mobile',20000,30,'Delhi');
insert into products values(3,'Boat earpods',3000,50,'Delhi');
insert into products values(4,'Levono Laptop',40000,15,'Mumbai');
insert into products values(5,'Charger',1000,0,'Mumbai');
insert into products values(6, 'Mac Book', 78000, 6, 'Delhi');
insert into products values(7, 'JBL speaker', 6000, 2, 'Delhi');

#Inserting values into customer table
insert into customer (cid, cname, age, addr) values
(101,'Ravi',30,'fdslfjl'),
(102,'Rahul',25,'fdslfjl'),
(103,'Simran',32,'fdslfjl'),
(104,'Purvesh',28,'fdslfjl'),
(105,'Sanjana',22,'fdslfjl');

#Inserting values into orders table
insert into orders values(10001,102,3,2700);
insert into orders values(10002,104,2,18000);
insert into orders values(10003,105,5,900);
insert into orders values(10004,101,1,46000);


#inserting values into payments table
insert into payment values(1,10001,2700,'upi','completed');
insert into payment values(2,10002,18000,'credit','completed');
insert into payment values(3,10003,900,'debit','in process');

update product
set locaiton = 'chennai'
where pname = 'Mac Book' ;

delete from customer
where cname = 'Ravi';




/* 
QUESTIONS
-- 0)Make a new table employee with specified column id, name, position and salary.
-- 1)insert query adds a new row to the employees table with specific values for id, name, position, and salary.
-- 2)update query updates the salary of the employee with id = 1.
-- 3)delete query deletes the row from employees where id = 1.
-- 4)create a query that creates a table called students.
-- 5)create another table courses and set up a foreign key constraint in the students table.
	The foreign key constraint ensures that the course_id in students must refer to a valid course_id in the courses table.
-- 6)Alter the students table to add the foreign key constraint.
-- 7)insert some data into the students table while respecting the constraints.
-- 8)create a SELECT query that retrieves products based on numeric and date conditions.
-- 9)update a record and set the last_updated column to the current datetime.
-- 10)delete products with stock below a certain threshold.
*/







--  insert  query adds a new row to the employees table with specific values for id, name, position, and salary.
INSERT INTO employees (id, name, position, salary)
VALUES (1, 'John Doe', 'Software Engineer', 75000);

-- update query updates the salary of the employee with id = 1.
UPDATE employees
SET salary = 80000
WHERE id = 1;

-- delete query deletes the row from employees where id = 1.
DELETE FROM employees
WHERE id = 1;

--  create a query that creates a table called students with various constraints.
CREATE TABLE students (
  student_id INT PRIMARY KEY,       
  name VARCHAR(100) NOT NULL,        
  email VARCHAR(100) UNIQUE,       
  age INT CHECK (age >= 18),        
  course_id INT,                    
  grade CHAR(1) DEFAULT 'F'          
);

-- create another table courses and set up a foreign key constraint in the students table. 
-- The foreign key constraint ensures that the course_id in students must refer to a valid course_id in the courses table.
CREATE TABLE courses (
  course_id INT PRIMARY KEY,          
  course_name VARCHAR(100) NOT NULL   
);

-- Alter the students table to add the foreign key constraint
ALTER TABLE students
ADD CONSTRAINT fk_course
FOREIGN KEY (course_id)
REFERENCES courses (course_id)
ON DELETE CASCADE;  -- If a course is deleted, all related students are also deleted

--  insert some data into the students table while respecting the constraints.

INSERT INTO students (student_id, name, email, age, course_id, grade)
VALUES (1, 'Alice Johnson', 'alice@example.com', 21, 101, 'A');  

-- This will fail because 'student_id' is not unique
INSERT INTO students (student_id, name, email, age, course_id, grade)
VALUES (1, 'Bob Smith', 'bob@example.com', 22, 102, 'B');  

-- This will also fail because 'name' has a NOT NULL constraint
INSERT INTO students (student_id, email, age, course_id, grade)
VALUES (3, 'charlie@example.com', 19, 103, 'B'); 

-- This will fail because 'age' doesn't meet the CHECK constraint
INSERT INTO students (student_id, name, email, age, course_id, grade)
VALUES (4, 'David Brown', 'david@example.com', 16, 104, 'C');  

--  create a SELECT query that retrieves products based on numeric and date conditions.
-- Retrieve products with a price greater than 100 and released after January 1, 2022
SELECT * 
FROM products 
WHERE price > 100 AND release_date > '2022-01-01';

--   update a record and set the last_updated column to the current datetime.
-- Update product details and set the last_updated to the current timestamp
UPDATE products
SET price = 1100.00, last_updated = NOW()  
WHERE product_id = 1;

-- delete products with stock below a certain threshold.
-- Delete products with stock below 100
DELETE FROM products 
WHERE stock < 100;

-- 3)
SELECT * FROM customers WHERE NOT city = 'New York';
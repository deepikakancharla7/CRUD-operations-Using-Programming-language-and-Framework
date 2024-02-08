# SQL and Django CRUD Operations for Registration Table

This project demonstrates how to perform CRUD (Create, Read, Update, Delete) operations using SQL and Django framework for a "Registration" table.

## SQL Query

The SQL query to create the "Registration" table is as follows:

```sql
CREATE TABLE Registration (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    DateOfBirth DATE,
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    IsActive BOOLEAN DEFAULT TRUE
);
This SQL query creates a table named "Registration" with columns for ID, Name, Email, DateOfBirth, RegistrationDate, and IsActive.


## Writing CRUD Operations

You can implement CRUD operations for the "Registration" table using Django views and forms. Here's an example of how to implement CRUD operations:

Create: Use Django forms to handle form submission and create new records in the database.
Read: Retrieve records from the database using Django ORM queries.
Update: Update existing records in the database using Django forms.
Delete: Delete records from the database using Django ORM queries.
You can write CRUD operation functions in Django views (views.py) and use Django forms (forms.py) for form handling and validation.

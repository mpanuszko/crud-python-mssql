# Product Management System - Northwind Database
A simple crud for Northwind DB made on Python

## Table of Contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Simple code example](#simple-code-example)
* [Technologies](#technologies)
* [Instalation](#instalation)
* [Licence](#licence)

## General info
This project is simple CRUD desktop app. CRUD stands for Create, Read, Update, Delete, and it is a common way to view, and modify data. This application is used to modify the products in the Northwind database. Python connects the application with Northwind Database via ODBC drivers.

## Screenshots
![Algorithm schema](./crud-python-mssql/app.jpg)

## Simple code example
     ```def view(self):
          self.cursor.execute("SELECT * FROM products")
          rows = self.cursor.fetchall()
          return rows

     def insert(self, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel,  Discontinued):
          self.cursor.execute("INSERT INTO products VALUES (?,?,?,?,?,?,?,?,?);", (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued))
          self.con.commit()```

## Technologies
Project is created with:
* Microsoft SQL Server 2014
* Python 3.7
* Tkinter library
* Pyodbc drivers

## Instalation
### Prerequisites
The application requires the installation of the MSSQL with SSMS and Python.
### Requirements
Open and Run Northwind-script in a new query window in SSMS.
For the application to work properly you need to install Microsoft ODBC Driver for SQL Server and Python SQL Driver - pyodbc.

## Licence
This project is licensed under the MIT License - see the LICENSE.md file for details.

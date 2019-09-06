import pyodbc

server = 'local server'
database = 'Northwind'
username = '***'
password = '***'

con = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    

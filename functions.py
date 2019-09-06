from config import con

 
class DataBase:
    
    def __init__(self):
        self.con = con
        self.cursor = con.cursor()
        self.con.commit()
        
    def __del__(self):
        self.con.close()
    
    def view(self):
        self.cursor.execute("SELECT * FROM products")
        rows = self.cursor.fetchall()
        return rows
        
    def insert(self, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued):
        self.cursor.execute("INSERT INTO products VALUES (?,?,?,?,?,?,?,?,?);", (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued))
        self.con.commit()

    def update(self, ProductID, ProductName="", SupplierID="", CategoryID="", QuantityPerUnit="", UnitPrice=""):
        self.cursor.execute("UPDATE products SET ProductName=?, SupplierID=?, CategoryID=?, QuantityPerUnit=?, UnitPrice=? WHERE ProductID=?", (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, ProductID))
        self.view()
        self.con.commit()
    
    def delete(self, ProductID):
        self.cursor.execute("DELETE FROM products WHERE ProductID=?", (ProductID,))
        self.con.commit()
    
    def search(self, ProductName="", SupplierID="", CategoryID="", QuantityPerUnit="", UnitPrice=""):
        self.cursor.execute("SELECT * FROM products WHERE ProductName=? OR SupplierID=? OR CategoryID=? OR QuantityPerUnit=? OR UnitPrice=?", (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice))
        rows = self.cursor.fetchall()
        return rows

        
db = DataBase()


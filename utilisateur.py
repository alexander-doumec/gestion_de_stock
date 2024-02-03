from product import Product
from category import Category
from store import Db

class Utilisateur : 
    def __init__(self) -> None:
        self.product = Product()
        self.category = Category()

    def createProduct(self, name, description,quantity,price,id_category):
        self.product.create(name, description,price, quantity, id_category)
    
    def readProcduct(self):
        return self.product.read()
    
    def updateProduct(self, id, name, description, quantity,price, id_category):
        self.product.update(id, name,description,quantity,price,id_category)

    def deleteProduct(self, id):
        self.product.delete(id)

    def findProduct(self, id):
        return self.product.find(id)
    
    def createCategory(self, name):
        self.category.create(name)

    def readCategory(self):
        return self.category.read()
    
    def updateCategory(self, id, name):
        self.category.update(id, name)

    def deleteCategory(self, id):
        self.category.delete(id)

    def findCategory(self, id):
        return self.category.find(id)
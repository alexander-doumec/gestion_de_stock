from product import Product
from store import Database

class Utilisateur:
    
    def __init__(self) -> None:
        self.product = Product()     
        

    def createProduct(self, name, description, price, quantity, id_category):
        self.product.create(name, description, price, quantity, id_category)
        return True

    def readproduit(self):
        return self.product.read()
    
    def updateproduit(self, id, name, description, price, quantity, id_category):
        self.product.update(id, name, description, price, quantity, id_category)
        return True
    
    def deleteproduit(self, id):
        self.product.delete(id)
        return True
    
    def findproduit(self, id):
        self.product.find(id)
        return True
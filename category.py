from store import Db

class Category : 
    def __init__(self):
        self.table = 'category'
        self.db = Db(host='localhost', user='root', password='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', database='store')


    def create(self, name):
        query = f'INSERT INTO {self.table} (name) VALUES (%s)'
        params = (name,)
        self.db.executeQuery(query, params)

    def read(self):
        query = f'Select * from category'
        return self.db.fetch(query)
    
    def update(self, name, id):
        query = f'UPDATE category SET name=%s WHERE id=%s'
        params = (name, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = f'DELETE FROM category WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)

    def find(self, id):
        query = f'SELECT * FROM category WHERE id=%s'
        params = (id,)
        return self.db.fetch(query, params)
    
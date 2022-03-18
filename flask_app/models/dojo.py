from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # get all dojos 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        if results:
            for row in results:
                dojos.append(row)
            return dojos


    # adds new created dojos to sql db
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)


    # get only 1 dojo showing all the ninjas in the dojo
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s "
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        if results:
            ninja = cls(results[0])
            ninja_data = []
            for row in results:
                data= {
                    "name": row["name"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "age": row["age"]
                }
                ninja_data.append(data)
            
            return ninja_data

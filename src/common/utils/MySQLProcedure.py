from typing import Any, List


class MySQLConnection:
    def __init__(self, **options):
        from MySQLdb import Connect
        self.connection = Connect(**options)


class MySQLCommand:
    parameters: List[str] = []
    stored_procedure: str = None
    result: List[dict] = []
    __cursor = None
    
    def __init__(self, connection):
        self.connection = connection

    def close(self):
        self.__cursor.close()

    def call_stored_procedure(self, name_stored_procedure: str):
        self.stored_procedure = name_stored_procedure
        self.__cursor = self.connection.cursor()
        self.__cursor.callproc(name_stored_procedure, self.parameters)

    def create_dict_from_cursor(self): 
        "Returns all rows from a cursor as a dict" 
        desc = self.__cursor.description 
        self.result = [
            dict(zip([col[0] for col in desc], row)) 
            for row in self.__cursor.fetchall() 
        ]
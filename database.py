import sqlite3

class Database:
    def __init__(self, database_file: str):
        '''Open database file.'''
        self.__datafile_name = database_file
        self.__data_connect = sqlite3.connect(database_file)
        self.__data_cursor = self.__data_connect.cursor()

    def __repr__(self):
        return f'<Database ({self.__datafile_name})>'

    def kill(self):
        self.__data_connect.commit()
        self.__data_connect.close()
    
    def select(columns: str, table_name: str, uslovie: str = None) -> list:
        '''execute command "SELECT [quaries] FROM table_name WHERE [uslovie];" if uslovie =/= None or "SELECT [quaries] FROM table_name;" if uslovie = None and return result.'''
        quire = f'SELECT {quaries} FROM {table_name}' + (f' WHERE {uslovie}' if uslovie else '') + ';'
        data = self.__data_cursor.execute(quire.replace('"', '').replace("'", "").replace('--', '')).fetchall()
        if len(data) == 1: return data[0]
        else: return data

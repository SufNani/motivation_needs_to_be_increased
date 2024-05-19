import sqlite3

class Database:
    def __init__(self, database_file: str):
        '''Open database file.'''
        self.__datafile_name = database_file
        self.__data_connect = sqlite3.connect(database_file)
        self.__data_cursor = self.__data_connect.cursor()
        self.execute = self.__data_cursor.execute

    def __repr__(self):
        return f'<Database ({self.__datafile_name})>'

    def kill(self):
        self.__data_connect.commit()
        self.__data_connect.close()

    def get_columns(self, table_name: str) -> list:
        return [e[0] for e in self.__data_cursor.execute(f'SELECT * FROM {table_name}'.replace('"', '').replace("'", "").replace('--', '')).description]

    def select(self, columns: str, table_name: str, groupby_column: str = None, uslovie: str = None, JSON: bool = True):
        '''execute command "SELECT [quaries] FROM table_name WHERE [uslovie];" if uslovie =/= None or "SELECT [quaries] FROM table_name;" if uslovie = None and return result if json-format if JSON option is set True, else list.'''
        quire = f'SELECT ' + ((groupby_column + ' ') if groupby_column else '') + f'{columns} FROM {table_name}' + (f' WHERE {uslovie}' if uslovie else '') + ';'
        data = self.execute(quire.replace('--', '')).fetchall()
        if not JSON:
            if len(data) == 1: return data[0]
            else: return data
        rdata = {}
        columns = columns.split(', ')
        for elm in data:
            rdata[elm[0]] = {}
            for i in range(len(elm)):
                rdata[elm[0]][columns[i]] = elm[i]
        return rdata

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
        columns = columns.replace(' ', '').split(',')
        if groupby_column:
            for elm in data:
                rdata[elm[0]] = {}
                for i in range(len(elm)):
                    rdata[elm[0]][columns[i]] = elm[i]
        else:
            if len(data) == 1:
                rdata = {}
                elm = data[0]
                for i in range(len(elm)):
                    rdata[columns[i]] = elm[i]
            else:
                rdata = []
                for elm in data:
                    rldata = {}
                    for i in range(len(elm)):
                        rldata[columns[i]] = elm[i]
                    rdata.append(rldata)

        return rdata

def json_merge(*dicts):
    rdict = {}
    for dt in dicts:
        for elm in dt:
            rdict[elm] = dt[elm]
    return rdict

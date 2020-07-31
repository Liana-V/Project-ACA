import sqlite3
import json


class InvalidTableStructure(Exception):
    pass


class DbMgr:

    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        if self.conn:
            self.close()

    def close(self):
        self.conn.close()
        self.conn = None

    def exec(self, query: str, params: list = list()):
        cursor = self.conn.cursor()
        try:
            if params:
                cursor.executemany(query, params)
            else:
                cursor.execute(query)

            self.conn.commit()
            return cursor
        except sqlite3.DatabaseError as dbex:
            self.conn.rollback()
            raise dbex

    def insert(self, table: str, columns: tuple, values: tuple):
        return self.exec(
            f'INSERT INTO {table}({", ".join(columns)})'
            f' VALUES ({", ".join(["?"] * len(values))});',
            values
        )
    def insert_json_to_db(self,table_name: str,file_name:str):
        with open(file_name, encoding='utf-8-sig') as json_file:
            json_data = json.loads(json_file.read())
            columns = []
            column = []
            for data in json_data:
                column = list(data.keys())
                for col in column:
                    if col not in columns:
                        columns.append(col)
            # Here we get values of the columns in the JSON file in the right order.
            value = []
            values = []
            for data in json_data:
                for i in columns:
                    value.append(str(dict(data).get(i)))
                values.append(list(value))
                value.clear()
            #
            # # Time to generate the create and insert queries and apply it to the sqlite3 database
            create_query = "create table if not exists {0} ({1})".format(table_name, " text,".join(columns))
            insert_query = "insert into {0} ({1})values(?{2})".format(table_name, ", ".join(columns),
                                                                       ",?" * (len(columns) - 1))

        self.exec(create_query) #piti estex avelacnel vor creat amenaskzbum lini
        return self.exec(insert_query, values)


    def select(self,table_name:str,param:str):
        select_query = "select id from skills where title = 'Hindi'"
        records=self.exec(select_query).fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id:  ", records[0])

            print("\n")

if __name__ == '__main__':
    dbase = DbMgr('new_sql.db')
    dbase.insert_json_to_db('jobs','data.json')

    dbase.insert_json_to_db('skills','skill.json')
    dbase.select('skills','AI')
import sqlite3
import json

def drop(cursor,table_name:str):
    drop_query = "DROP TABLE IF  EXISTS  {}".format(table_name)
    cursor.execute(drop_query)
    return cursor


def insert_json_to_db(cursor,table_name:str,file_name:str):
    with open(file_name, encoding='utf-8-sig') as json_file:
        json_data = json.loads(json_file.read())
        print(table_name)
        columns = []
        column = []
        for data in json_data:
            column = list(data.keys())
            for col in column:
                if col not in columns:
                    columns.append(col)
        value = []
        values = []
        for data in json_data:
            for i in columns:
                value.append(str(dict(data).get(i)))
            values.append(list(value))
            value.clear()
        print(values)

        create_query = "create table if not exists {0} ({1})".format(table_name, " text,".join(columns))
        insert_query = "insert into {0} ({1})values(?{2})".format(table_name, ", ".join(columns),
                                                                   ",?" * (len(columns) - 1))

    cursor.execute(create_query)
    cursor.executemany(insert_query, values)


    return cursor

def find(find,table_name,find_by):
    conn = sqlite3.connect("my_db.db")
    cursor = conn.cursor()
    FIND="SELECT {0}  FROM {1} WHERE title = '{2}';".format(find,table_name,find_by)
    a=cursor.execute(FIND).fetchall()[0][0]
    return int(a)
# def select(cursor,table_name:str,param:str):
#     select_query = "select id from skills where title = 'Hindi'"
#     records=self.exec(select_query).fetchall()
#     print("Total rows are:  ", len(records))
#     print("Printing each row")
#     for row in records:
#         print("Id:  ", records[0])
#         print("\n")


import sqlite3
import json

def drop(cursor,table_name:str):
    drop_query = "DROP TABLE IF  EXISTS {}".format(table_name)
    cursor.execute(drop_query)
    return cursor


def insert_json_to_db(cursor,table_name:str,file_name:str):
    with open(file_name, encoding='utf-8-sig') as json_file:
        json_data = json.loads(json_file.read())
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
                value.append((dict(data).get(i)))
            values.append(list(value))
            value.clear()
        id='id INTEGER PRIMARY KEY ,'
        create_query = "create table if not exists {0} ({1}{2})".format(table_name, id," text,".join(columns[1:]))
        insert_query = "insert or replace into {0} ({1})values(?{2})".format(table_name, ", ".join(columns),
                                                                   ",?" * (len(columns) - 1))

    cursor.execute(create_query)
    cursor.executemany(insert_query, values)


    return cursor

def find(find,table_name,find_by):
    conn = sqlite3.connect("my_db.db")
    cursor = conn.cursor()
    FIND="SELECT {0}  FROM {1} WHERE title = '{2}';".format(find,table_name,find_by)
    try:
        a=cursor.execute(FIND).fetchall()[0][0]
    except Exception as ex:
        a=0
    return int(a)
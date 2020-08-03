import sqlite3
from db.dbmgr import insert_json_to_db
from scrap.scrap import job_scrap


def create_db():
    conn = sqlite3.connect("my_db.db")
    cursor = conn.cursor()
    with open("db/database.sql", "r") as file:
        cursor.executescript(file.read())
    # drop(cursor, 'SKILLS')
    insert_json_to_db(cursor, 'SKILLS', 'scrap/skill.json')

    job_scrap()
    # drop(cursor, 'JOBS')
    insert_json_to_db(cursor, 'JOBS', 'scrap/data.json')
    conn.commit()

    conn.close()

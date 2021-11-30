import sqlite3
import random

database = sqlite3.connect("planirovka_server.sqlite3")
sql = database.cursor()

# sql.execute(
#     """
#     CREATE TABLE todo(
#        id INT,
#        time TEXT,
#        plan TEXT,
#        done BIT
#     )
#     """
# )

database.commit()


def planirovka():
    global todo_id, todo_time, todo_plan, todo_done
    planirovka_id = input('id: ')
    planirovka_time = input('time: ')
    planirovka_plan = input('plan: ')
    planirovka_done = input('done: ')

    sql.execute(f"SELECT id FROM todo WHERE id = '{planirovka_id}'")
    done = random.randint(0, 1)
    if sql.fetchone() is None:
        sql.execute("INSERT INTO todo VALUES (?,?,?,?)",
                    (planirovka_id,planirovka_time, planirovka_plan, planirovka_done))
        sql.execute("SELECT * FROM planirovka;")
        print(planirovka_id, planirovka_time, planirovka_plan, planirovka_done)

        database.commit()
        print("Planirovka  allready done!!!")
    else:
        print("Planirovka is not done!")
        for values in sql.execute("SELECT * FROM todo"):
            print(values)

planirovka()

def deletedonelist():
    sql.execute("DELETE FROM todo WHERE done = 1;")
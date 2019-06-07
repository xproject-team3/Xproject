import sqlite3
def create_table():
    conn = sqlite3.connect("distance.db")
    cur = conn.cursor()
    cur.execute('''create table DIS(DATE, DIS)
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()

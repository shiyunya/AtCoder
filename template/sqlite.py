import sqlite3

def get_cur():
    con = sqlite3.connect(':memory:', isolation_level=None)
    cur = con.cursor()
    # 高速化の設定
    cur.executescript("""
    PRAGMA trusted_schema = OFF;
    PRAGMA journal_mode = OFF;
    PRAGMA synchronous = OFF;
    PRAGMA temp_store = memory;
    PRAGMA secure_delete = OFF;
    """)
    return cur

cur = get_cur()
cur.executescript("""
CREATE TABLE sample(id INT, value INT);
CREATE INDEX sample_idx ON sample(id);
""")

for i in range(10):
    cur.execute("INSERT INTO sample VALUES(?, ?)", [i, i * i])

cur.execute("SELECT * FROM sample ORDER BY value DESC")
values = cur.fetchall()
print(values)
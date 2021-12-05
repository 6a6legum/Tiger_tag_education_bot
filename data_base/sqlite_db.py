import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('users.db')
    cur = base.cursor()
    if base:
        print("Database connected OK")

    base.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, category TEXT, recieve_news TEXT, intro_test_score INTEGER)')
    base.commit()

async def sql_update_users(state, id):
    async with state.proxy() as data:
        cur.execute('''UPDATE users SET id = ?, name= ? , category = ?, recieve_news = ?, intro_test_score = ?  WHERE id = ?''', (data.get("id"), data.get("name"), data.get("category"), data.get("recieve"), data.get("intro_test"), id))
        base.commit()

async def sql_update_intro_test_level(score, id):
    cur.execute('''UPDATE users SET intro_test_score = ?  WHERE id = ?''', (score, id))
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(id):
    cur.execute("SELECT * FROM users WHERE id=:_id", {"_id": id})
    return cur.fetchall()
    # base.commit()
    # for ret in cur.execute('SELECT * FROM users').fetchall():
    # pass
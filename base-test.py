import sqlite3

connection = sqlite3.connect('test.db')

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS News (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp TEXT NOT NULL)""")

cursor.execute('CREATE INDEX idx_title ON News (title)')

cursor.execute('INSERT INTO News (title, content, timestamp) VALUES (?, ?, ?)', 
    ("Эксперты оценили уровень потерь ВВП России из-за дефицита кадров", "test", "Mon Dec  4 06:56:35 2023",))


connection.commit()
connection.close()
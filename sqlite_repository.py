import sqlite3

class SqliteRepository(object):
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self._create()

    def _create(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS Person (name text, surname text, phone_number text, email text) ''')

    def put(self, name, surname, phone_number, email):
        self.conn.execute('''INSERT INTO person VALUES (?, ?, ? , ?)''', (name, surname, phone_number, email))

    def find_all(self):
        cursor = self.conn.execute('''SELECT * FROM person''')
        return cursor.fetchall()

    def find_by_email(self, email):
        cursor = self.conn.execute('''SELECT * FROM person WHERE email="{email}"'''.format(email=email))
        name, surname, phone_number, email = cursor.fetchone()
        return {'name': name,
                'surname': surname,
                'phone_number': phone_number,
                'email': email}



class Database:


    def __init__(self, db_file_name='./lightmeter,db'):
        import sqlite3

        self.CREATE_CURRENT_TABLE = """CREATE TABLE IF NOT EXISTS panel_current (
               timestamp_utc REAL PRIMARY KEY,
               _current REAL,
               light REAL);"""

        self.CREATE_VOLTAGE_TABLE = """CREATE TABLE IF NOT EXISTS panel_voltage (
                   timestamp_utc REAL PRIMARY KEY,
                   voltage REAL,
                   light REAL);"""

        self.INSERT_VOLTAGE = """INSERT INTO panel_voltage (timestamp_utc, voltage, light) VALUES (CURRENT_TIMESTAMP, ?, ?);"""
        self.INSERT_CURRENT = """INSERT INTO panel_current (timestamp_utc, _current, light) VALUES (CURRENT_TIMESTAMP, ?, ?);"""

        self.conenction = sqlite3.connect(db_file_name)

    def __del__(self):
        self.conenction.close()

    def execute(self, query):
        with self.conenction as connetion:
            connetion.execute(query)

    def create_tables(self):
        self.execute(self.CREATE_VOLTAGE_TABLE)
        self.execute(self.CREATE_CURRENT_TABLE)

    def insert_voltage_reading(self, voltage, light_intensity):
        with self.conenction as connection:
            connection.execute(self.INSERT_VOLTAGE, (voltage, light_intensity))

    def insert_current_reading(self, current, light_intensity):
        with self.conenction as connection:
            connection.execute(self.INSERT_CURRENT, (current, light_intensity))

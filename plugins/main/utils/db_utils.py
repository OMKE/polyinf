import mysql.connector
import hashlib

def connection(host, user, password, self):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.current_connection = mydb
        self.current_cursor=self.current_connection.cursor()
        return mydb
    except mysql.connector.Error as err:
        print(err)
        raise


def use_database(database_name, self):
    self.current_cursor.execute("USE {}".format(database_name))


def get_all_tables(self):
    self.current_cursor.execute("Show tables;")
    records = self.current_cursor.fetchall()
    return list(map(lambda record: ''.join(record), records))

def get_table_data(self, table_name):
    self.current_cursor.execute("select * from `" + table_name + "`")
    records = self.current_cursor.fetchall()
    column_names = [i[0] for i in self.current_cursor.description]
    return [column_names, records]

   
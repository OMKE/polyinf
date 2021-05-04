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

def get_users(self):
    users = None
    self.current_cursor.callproc("get_all_users")
    for i in self.current_cursor.stored_results():
        users = i.fetchall()
    return users

def promote_user(self, user_id):
    self.current_cursor.callproc("promote_user", user_id)
    self.current_connection.commit()
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


def get_all_columns(self):
    columns = []
    columns_sorted = []
    current_cordinates = 280

    self.current_cursor.callproc("show_users_columns")
    for i in self.current_cursor.stored_results():
        columns = i.fetchall()

    for i in columns:
        if i[0] != "USER_ID" and i[0] != "USER_ROLE":
            columns_sorted.append({
                    "name" : i[0].replace('USER_', '').lower(),
                    "display_name": i[0].replace('USER_', '').replace("_", " ").capitalize(),
                    "cordinates": current_cordinates
                })
            current_cordinates += 40

    return columns_sorted

def register_user(self, first_name, last_name, email, password):

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    self.current_cursor.callproc("create_user", (first_name, last_name, email, hashed_password))
    self.first_name.setText("")
    self.last_name.setText("")
    self.email.setText("")
    self.password.setText("")
    self.current_connection.commit()
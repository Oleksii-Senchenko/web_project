import sqlite3
from user_system import AccountManager

connection = sqlite3.connect("users_data.db")
cursor = connection.cursor()

users_table = """CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE,
  email TEXT UNIQUE,
  password TEXT

)"""


# cursor.execute(users_table)
# connection.commit()
#
# connection.close()


class User:
    def __init__(self):
        self.current_user = None

    def register_user(self, username, email, password):
        try:
            connection = sqlite3.connect("users_data.db")
            cursor = connection.cursor()

            new_user = """
                 INSERT INTO users (username, email, password )
                 VALUES (?, ?, ?)
                 """

            cursor.execute(new_user, (username, email, password))
            connection.commit()
            print("Success")

        except sqlite3.IntegrityError as e:
            return f"User {username} already exists"
        finally:
            connection.close()

    def login_user(self, email, password):
        connection = sqlite3.connect("users_data.db")
        cursor = connection.cursor()

        wanted_user = "select id, username from users where email = ? and password = ?"
        cursor.execute(wanted_user, (email, password))
        user = cursor.fetchone()
        connection.close()

        if user:
            user_id, username = user
            self.current_user = user[0]
            print(f"Wellcome, {username}!")
            return True
        else:
            print("Username or password is wrong!")
            return False

    def logout_user(self):
        self.current_user = None


testik_ = User()



def main():
    user_system = User()

    print("\nChose option:")
    print("1 - Register")
    print("2 - Login")
    print("3 - Logout")

    choice = input("Your chose: ").strip()

    if choice == "1":
        username = input("Enter username: ").strip()
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()

        user_system.register_user(username,email, password)

    elif choice == "2":
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()
        user_system.login_user(email, password)

    elif choice == "3":
        print("Logged out.")




# main()



user_system = User()
user_system.register_user("testuser", "test@example.com", "12345")

if user_system.login_user("test@example.com", "12345"):
    user_id = user_system.current_user

    site_system = AccountManager(user_id)

    site_system.add_account("Facebook", "fb_user", "fb_pass", "Facebook")
    site_system.add_account("Google", "google_user", "google_pass", "Google")

    regs = site_system.get_registrations()
    print("\nUser registrations:")
    for reg in regs:
        print(f"Site: {reg[0]}, Login: {reg[1]}, Type: {reg[2]}")

    site_system.delete_registration("Facebook")

    regs = site_system.get_registrations()
    print("\nRegistrations after deletion:")
    for reg in regs:
        print(f"Site: {reg[0]}, Login: {reg[1]}, Type: {reg[2]}")
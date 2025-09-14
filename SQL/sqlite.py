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
        connection = sqlite3.connect("users_data.db")
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, password)
            )
            connection.commit()
            print(f"User {username} has been successfully registered!")
        except sqlite3.IntegrityError:
            print("A user with this username or email already exists.")
        finally:
            connection.close()

    def login_user(self, email, password):
        connection = sqlite3.connect("users_data.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, username FROM users WHERE email = ? AND password = ?",
            (email, password)
        )
        user = cursor.fetchone()
        connection.close()
        if user:
            self.current_user = user[0]
            print(f"Welcome, {user[1]}!")
            return True
        else:
            print("Incorrect email or password.")
            return False

    def logout_user(self):
        self.current_user = None



testik_ = User()


def main():
    user_system = User()

    while True:
        print("\nChoose an option:")
        print("1 - Register")
        print("2 - Login")
        print("3 - Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            email = input("Enter email: ").strip()
            password = input("Enter password: ").strip()
            user_system.register_user(username, email, password)

        elif choice == "2":
            email = input("Enter email: ").strip()
            password = input("Enter password: ").strip()
            if user_system.login_user(email, password):
                user_id = user_system.current_user
                account_manager = AccountManager(user_id)
                while True:
                    print("\nAccount Menu:")
                    print("1 - Add account")
                    print("2 - Show all accounts")
                    print("3 - Return to main menu")
                    acc_choice = input("Your choice: ").strip()

                    if acc_choice == "1":
                        site_name = input("Enter site name: ").strip()
                        auth_type = input("Enter authentication type: ").strip()
                        account_manager.add_account(site_name, auth_type=auth_type)

                    elif acc_choice == "2":
                        regs = account_manager.get_registrations()
                        if regs:
                            print("\nYour accounts:")
                            for reg in regs:
                                print(f"Site: {reg[0]}, Login: {reg[1]}, Type: {reg[2]}")
                        else:
                            print("No accounts added.")

                    elif acc_choice == "3":
                        print("Returning to main menu.")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()



# main()




import sqlite3


class AccountManager:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_account(self, site_name, login, password, auth_type):
        connection = sqlite3.connect("users_data.db")
        cursor = connection.cursor()

        query = """
            INSERT INTO user_accounts (site_name, login, password, auth_type, user_id)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (site_name, login, password, auth_type, self.user_id))
        connection.commit()
        connection.close()
        print("Account added successfully!")

    def get_registrations(self):
        connection = sqlite3.connect("users_data.db")
        cursor = connection.cursor()

        cursor.execute("SELECT site_name, login, auth_type FROM user_accounts WHERE user_id = ?", (self.user_id,))
        registrations = cursor.fetchall()
        connection.close()
        return registrations

    def delete_registration(self, site_name):
        connection = sqlite3.connect("users_data.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM user_accounts WHERE user_id = ? AND site_name = ?", (self.user_id, site_name))
        connection.commit()
        connection.close()
        print(f"Registration for {site_name} deleted successfully.")

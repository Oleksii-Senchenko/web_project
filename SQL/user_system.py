import sqlite3


class AccountManager:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_account(self, site_name, login=None, password=None, auth_type=None):
        connection = sqlite3.connect("users_data.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id FROM user_accounts WHERE user_id = ? AND site_name = ? AND auth_type = ?",
            (self.user_id, site_name, auth_type)
        )
        existing = cursor.fetchone()

        if existing:
            print(f"The site '{site_name}' with authentication type '{auth_type}' is already added. Login and password are not needed.")
        else:
            # If data is not provided, ask for it
            if login is None:
                login = input(f"Enter login for {site_name}: ").strip()
            if password is None:
                password = input(f"Enter password for {site_name}: ").strip()
            if auth_type is None:
                auth_type = input(f"Enter authentication type for {site_name}: ").strip()

            cursor.execute(
                "INSERT INTO user_accounts (site_name, login, password, auth_type, user_id) VALUES (?, ?, ?, ?, ?)",
                (site_name, login, password, auth_type, self.user_id)
            )
            connection.commit()
            print(f"Account for {site_name} has been successfully added!")
        connection.close()

    def get_registrations(self):
        connection = sqlite3.connect("users_data.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT site_name, login, auth_type FROM user_accounts WHERE user_id = ?",
            (self.user_id,)
        )
        registrations = cursor.fetchall()
        connection.close()
        return registrations

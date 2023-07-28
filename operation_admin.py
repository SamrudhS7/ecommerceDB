import time
from operation_user import UserOperations


class Admin:
    def register_admin(self):
        """
        Register the admin account if it has not been registered already.

        This method reads the user data from the "users.txt" file and checks if an admin account
        already exists. If not, it generates a unique admin ID, sets a default admin name and password,
        encrypts the password, and writes the admin data to the "users.txt" file.

        Note: Make sure to set your desired password for the admin account in the line:
        `admin_password = "adminpass"`.
        """
        with open("data/users.txt", "r") as file:
            for line in file:
                user_info = eval(line)
                if user_info['user_role'] == 'admin':
                    # Admin account already registered
                    return

        u1 = UserOperations()
        admin_id = u1.generate_unique_user_id()
        admin_name = "admin"
        admin_password = "adminpass"  # Set your desired password for the admin account
        encrypted_password = u1.encrypt_password(admin_password)
        register_time = time.strftime("%Y-%m-%d %H:%M:%S")

        admin_data = {
            "user_id": admin_id,
            "user_name": admin_name,
            "user_password": encrypted_password,
            "user_role": "admin",
            "user_register_time": register_time
        }

        with open("data/users.txt", "a") as file:
            file.write(str(admin_data) + "\n")

# Testing the Admin class
# a1 = Admin()
# a1.register_admin()

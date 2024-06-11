from components.add_product import add_product_menu
from auth.auth import login_user, register_new_user
from components.cart_menu import cart_menu
from components.check_menu import check_out_menu
from db.db_init import db_main
from utils.menu_table import auth_menu, show_main_menu, welcome_banner
from utils.os_utils import farewell_message, file_exists, invalid_choice, wait_for_key


def main_menu():
    try:
        welcome_banner()

        while True:
            auth_menu()

            choice = input(f"\n\n[*] Enter the NUMBER of your choice: ")

            # Register
            if choice == "1":
                client = register_new_user()
                wait_for_key()

            # Login
            elif choice == "2":
                client = login_user()
                wait_for_key()

                if client:
                    user_menu(client)

            # Exit
            elif choice == "3":
                farewell_message()

            # Invalid choice
            else:
                invalid_choice()

    # ctrl + c
    except KeyboardInterrupt:
        print("\n\n[-] Program cancelled. Goodbye!\n\n")
        exit(0)

    # Unexpected error
    except Exception as error:
        print("\n\n[-] Oops! An unexpected error has occurred.")
        print(f"\n\n[-] Error: {error} \n\n")
        exit(1)


def user_menu(client):
    while True:
        show_main_menu()
        choice = input(
            f"\n\n[*] Enter the NUMBER of your choice: ")

        # Add product
        if choice == "1":
            add_product_menu(client)

        # My cart
        elif choice == "2":
            cart_menu(client)

        # Check Out
        elif choice == "3":
            check_out_menu(client)

        # Profile
        elif choice == "4":
            client.display_info()

        # Exit
        elif choice == "5":
            farewell_message()

        # Invalid choice
        else:
            invalid_choice()


if __name__ == "__main__":
    if not file_exists("inventory.pickle"):
        db_main()
        wait_for_key()

    main_menu()

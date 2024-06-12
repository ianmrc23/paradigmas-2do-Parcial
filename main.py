from components.add_menu import add_product_menu
from auth.auth import login_user, register_new_user
from components.cart_menu import cart_menu
from components.check_menu import check_out_menu
from db.db_init import db_main
from utils.menu_table import auth_menu, show_main_menu, welcome_banner
from utils.os_utils import clear_screen, farewell_message, file_exists, invalid_choice, wait_for_key


def main_menu():
    """
    Controla el flujo principal del programa, gestionando la autenticación y el acceso al menú de usuario.
    """
    try:
        welcome_banner()  # Muestra el banner de bienvenida

        while True:
            auth_menu()  # Muestra el menú de autenticación

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

    # Handle ctrl + c interruption
    except KeyboardInterrupt:
        print("\n\n[-] Program cancelled. Goodbye!\n\n")
        exit(0)

    # Handle unexpected errors
    except Exception as error:
        print("\n\n[-] Oops! An unexpected error has occurred.")
        print(f"\n\n[-] Error: {error} \n\n")
        exit(1)


def user_menu(client):
    """
    Muestra el menú principal del usuario y maneja las selecciones del usuario.

    Args:
        client (Client): El objeto cliente que ha iniciado sesión.
    """
    while True:
        show_main_menu()  # Muestra el menú principal
        choice = input(f"\n\n[*] Enter the NUMBER of your choice: ")

        if choice == "1":
            add_product_menu(client)

        elif choice == "2":
            cart_menu(client)

        elif choice == "3":
            check_out_menu(client)
            wait_for_key()

        elif choice == "4":
            clear_screen()
            client.display_info()
            wait_for_key()

        elif choice == "5":
            farewell_message()

        else:
            invalid_choice()


if __name__ == "__main__":
    if not file_exists("inventory.pickle"):
        db_main()
        wait_for_key()

    main_menu()

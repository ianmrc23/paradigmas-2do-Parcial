from schemas.client_manager import Client
from utils.menu_table import show_cart_menu
from utils.os_utils import clear_screen, invalid_choice, wait_for_key


def cart_menu(client: Client):
    while True:
        clear_screen()
        show_cart_menu()
        choice = input(
            f"\n\n[*] Enter the NUMBER of your choice or 0 to go back: ")

        if choice == '0':
            return

        elif choice == '1':
            clear_screen()
            client.view_cart()
            wait_for_key()

        elif choice == '2':
            clear_screen()
            client.remove_product()
            wait_for_key()

        elif choice == '3':
            clear_screen()
            client.clear_cart()
            wait_for_key()

        else:
            invalid_choice()

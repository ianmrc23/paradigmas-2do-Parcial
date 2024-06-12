from schemas.client_manager import Client
from utils.menu_table import show_cart_menu
from utils.os_utils import clear_screen, invalid_choice, wait_for_key


def cart_menu(client: Client):
    """
    Muestra el menú del carrito de compras y gestiona las opciones seleccionadas por el usuario.
    """
    while True:
        clear_screen()
        show_cart_menu()
        choice = input(
            "\n\n[*] Enter the NUMBER of your choice or 0 to go back: ")

        if choice == '0':
            # Regresar al menú principal
            return

        elif choice == '1':
            # Ver el carrito
            clear_screen()
            client.view_cart()
            wait_for_key()

        elif choice == '2':
            # Remover un producto del carrito
            clear_screen()
            client.remove_product()
            wait_for_key()

        elif choice == '3':
            # Limpiar el carrito
            clear_screen()
            client.clear_cart()
            wait_for_key()

        else:
            # Opción inválida
            invalid_choice()

from utils.os_utils import (
    clear_screen,
    wait_for_key,
    invalid_choice,
    load_pickle_file,
    save_pickle_file
)


def add_product_menu(client):
    """
    Muestra el menú para añadir productos al carrito del cliente.
    """
    categories = load_pickle_file("inventory.pickle")

    while True:
        clear_screen()
        show_categories(categories)
        choice = input(
            f"\n\n[*] Enter the NUMBER of your choice or 0 to go back: ")

        if choice == "0":
            return

        elif choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(categories):
                selected_category = list(categories.values())[choice - 1]
                show_products(categories, selected_category, client)

            else:
                invalid_choice()

        else:
            invalid_choice()


def show_products(categories, selected_category, client):
    """
    Muestra los productos disponibles en la categoría seleccionada y permite añadirlos al carrito.
    """
    while True:
        clear_screen()
        show_products_inCategory(selected_category)
        choice = input(
            f"\n\n[*] Enter the ID of the product you want or 0 to go back: ")

        if choice == "0":
            return

        elif choice.isdigit():
            product_number = int(choice)
            if 0 < product_number <= len(selected_category.products):
                selected_product = selected_category.products[product_number - 1]

                if selected_product.product_quantity > 0:
                    add_product(categories, selected_product, client)

                else:
                    print(
                        f"\n\n[-] Sorry, {selected_product.product_name} is out of stock.")
                    wait_for_key()

            else:
                invalid_choice()

        else:
            invalid_choice()


def add_product(categories, selected_product, client):
    """
    Añade el producto seleccionado al carrito del cliente.
    """
    while True:
        choice = input(
            f"\n\n[*] Enter the number of {selected_product.product_name}'s you want or 0 to go back: ")

        if choice == "0":
            return

        elif choice.isdigit():
            choice = int(choice)

            if choice > 0 and choice <= selected_product.product_quantity:
                selected_product.product_quantity -= choice

                client.add_to_cart(selected_product, choice)

                print(
                    f"\n\n[+] {choice} {selected_product.product_name}'s have been added to your cart.")

                save_pickle_file(client, f"{client.client_email}.pickle")
                save_pickle_file(categories, "inventory.pickle")

                wait_for_key()

                return

            else:
                invalid_choice()

        else:
            invalid_choice()


def show_categories(categories):
    """
    Muestra las categorías disponibles.
    """
    print(f"╔{'═' * 52}╗")
    print(f"║" + "AVAILABLE CATEGORIES".center(52) + "║")
    print(f"╠{'═' * 52}╣")
    for idx, category in enumerate(categories.values(), 1):
        print(f"║   {idx}. {category.category_name:<45} ║")
    print(f"╚{'═' * 52}╝")


def show_products_inCategory(selected_category):
    """
    Muestra los productos disponibles en una categoría específica.
    """
    print(f"╔{'═' * 52}╗")
    print(
        f"║" + f"Category: {selected_category.category_name}".center(52) + "║")
    print("╠════╦═══════════════════════════╦═══════╦═══════════╣")
    print("║ ID ║       Product Name        ║ Stock ║   Price   ║")
    print("╠════╬═══════════════════════════╬═══════╬═══════════╣")
    for idx, product in enumerate(selected_category.products, 1):
        print(
            f"║ {idx:<2} ║ {product.product_name:<25} ║ {product.product_quantity:<5} ║ ${product.product_price:<8} ║"
        )
    print("╚════╩═══════════════════════════╩═══════╩═══════════╝")

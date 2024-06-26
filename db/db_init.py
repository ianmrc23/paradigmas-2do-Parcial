from schemas.product_manager import Product, Category
from utils.os_utils import clear_screen, get_main_dir, load_pickle_file, save_pickle_file


def read_inventory():
    """
    Lee el archivo de inventario y crea un diccionario de categorías con sus respectivos productos.
    """
    categories = {}

    with open(get_main_dir("db/inventory.txt"), "r") as file:
        for line in file:
            parts = line.strip().split(" ")
            (
                category_id,
                category_name,
                product_id,
                product_name,
                product_price,
                product_quantity,
                product_weight,
            ) = parts

            category_id = int(category_id)
            product_id = int(product_id)
            product_price = float(product_price)
            product_quantity = int(product_quantity)
            product_weight = float(product_weight)

            if category_id not in categories:
                categories[category_id] = Category(category_id, category_name)

            product = Product(
                product_id,
                product_name,
                product_price,
                product_quantity,
                product_weight,
            )
            categories[category_id].products.append(product)

    return categories


def print_inventory():
    """
    Carga el inventario desde un archivo pickle y muestra las categorías y productos en un formato legible.
    """
    categories = load_pickle_file("inventory.pickle")
    clear_screen()
    print(f"{'═' * 100}")
    for category in categories.values():
        print(
            f"[+] Category ID: {category.category_id}\tName: {category.category_name}"
        )
        print("\nProducts:")
        for product in category.products:
            print(
                f"\tProduct ID: {product.product_id}, Name: {product.product_name}, Price: ${product.product_price}, Quantity: {product.product_quantity}, Weight: {product.product_weight}kg"
            )
        print(f"{'═' * 100}")


def db_main():
    """
    Lee el inventario desde un archivo de texto, lo guarda en un archivo pickle y notifica al usuario.
    """
    categories = read_inventory()
    save_pickle_file(categories, "inventory.pickle")
    print("\n\n[+] Inventory data has been saved as inventory.pickle")

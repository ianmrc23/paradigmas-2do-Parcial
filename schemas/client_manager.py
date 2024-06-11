from typing import List

from utils.os_utils import (
    invalid_choice,
    confirm_choice_input,
    load_pickle_file,
    save_pickle_file
)


class Client:
    def __init__(
        self,
        client_id: int,
        client_name: str,
        client_email: str,
        client_password: str,
        client_address: str,
        client_distance: float,
    ):
        self.client_id = client_id
        self.client_name = client_name
        self.client_email = client_email
        self.client_password = client_password
        self.client_address = client_address
        self.client_distance_from_store = client_distance
        self.cart: List[dict] = []

    def display_info(self):
        print(f"╔{'═' * 52}╗")
        print(f"║" + "CLIENT INFORMATION".center(52) + "║")
        print("╠════════════════════╦═══════════════════════════════╣")
        print(f"║   Client ID        ║ {self.client_id:<29} ║")
        print(f"║   Client Name      ║ {self.client_name:<29} ║")
        print(f"║   Client Email     ║ {self.client_email:<29} ║")
        print(f"║   Client Password  ║ {self.client_password:<29} ║")
        print(f"║   Client Address   ║ {self.client_address:<29} ║")
        print(
            f"║   Client Distance  ║ {self.client_distance_from_store:<29} ║")
        print("╚════════════════════╩═══════════════════════════════╝")

    def calculate_totals(self):
        total_price: float = 0.0
        total_weight: float = 0.0

        for item in self.cart:
            product = item["product"]
            quantity = item["quantity"]

            total_price += product.product_price * quantity
            total_weight += product.product_weight * quantity

        return total_price, total_weight

    def view_cart(self):
        if not self.cart:
            print("\n\n[+] Your cart is empty.")
            return

        total_price, total_weight = self.calculate_totals()
        total_price = "{:.2f}".format(total_price)
        total_weight = "{:.2f}".format(total_weight)

        print(f"╔{'═' * 52}╗")
        print("║" + "Your Cart".center(52) + "║")
        print("╠══════════════════════╦════════════╦════════════════╣")
        print("║ Product Name         ║  Quantity  ║      Price     ║")
        print("╠══════════════════════╬════════════╬════════════════╣")
        for item in self.cart:
            product = item["product"]
            quantity = item["quantity"]
            price = round(product.product_price * quantity, 2)
            print(
                f"║ {product.product_name.ljust(20)} ║  {str(quantity).ljust(9)} ║ $ {str(price).ljust(12)} ║")
        print("╠══════════════════════╩════════════╩════════════════╣")
        print(f"║ {'Total Price:'.ljust(35)} $ {total_price.ljust(12)} ║")
        print(f"║ {'Total Weight:'.ljust(35)}Kg {total_weight.ljust(12)} ║")
        print(f"╚{'═' * 52}╝")

    def add_to_cart(self, product, quantity):
        for item in self.cart:
            if item["product"].product_id == product.product_id:
                item["quantity"] += quantity
                break

        else:
            cart_item = {"product": product, "quantity": quantity}
            self.cart.append(cart_item)

        save_pickle_file(self, f"{self.client_email}.pickle")

    def remove_product(self):
        if not self.cart:
            print("\n\n[*] Your cart is already empty.")
            return

        while True:
            print_product_table(self.cart)

            choice = input(
                "\n\n[*] Enter the NUMBER of the product to remove or 0 to go back: ")

            if choice == "0":
                return

            elif choice.isdigit():
                product_number = int(choice)

                if 0 < product_number <= len(self.cart):
                    selected_product = self.cart[product_number - 1]["product"]
                    quantity_to_remove = self.cart[product_number - 1]["quantity"]

                    confirm_choice = confirm_choice_input(
                        f"\n\n[*] Are you sure you want to remove {quantity_to_remove} {selected_product.product_name}'s? (y/n): "
                    )

                    if confirm_choice == "y":
                        self.cart.pop(product_number - 1)

                        categories = load_pickle_file("inventory.pickle")
                        for category in categories.values():
                            for prod in category.products:
                                if prod.product_id == selected_product.product_id:
                                    prod.product_quantity += quantity_to_remove
                                    break

                        save_pickle_file(categories, "inventory.pickle")

                        save_pickle_file(self, f"{self.client_email}.pickle")

                        print(
                            f"\n\n[+] {quantity_to_remove} {selected_product.product_name}'s have been removed from your cart."
                        )
                        return

                    elif confirm_choice == "n":
                        print("\n\n[-] Operation canceled.")

                else:
                    invalid_choice()

            else:
                invalid_choice()

    def clear_cart(self):
        if not self.cart:
            print("\n\n[*] Your cart is already empty.")
            return

        print("\n\n[+] Your cart contains the following items:\n")
        print_product_table(self.cart)

        confirm_choice = confirm_choice_input(
            "\n\n[*] Are you sure you want to clear your cart? (y/n): "
        )

        if confirm_choice == "y":
            categories = load_pickle_file("inventory.pickle")

            for item in self.cart:
                product = item["product"]
                quantity_to_add_back = item["quantity"]
                for category in categories.values():
                    for prod in category.products:
                        if prod.product_id == product.product_id:
                            prod.product_quantity += quantity_to_add_back
                            break

            save_pickle_file(categories, "inventory.pickle")

            self.cart.clear()

            save_pickle_file(self, f"{self.client_email}.pickle")

            print("\n\n[+] Your cart has been successfully cleared.")

        elif confirm_choice == "n":
            print("\n\n[-] Cart clearing canceled.")


def print_product_table(cart):
    print(f"╔{'═' * 52}╗")
    print(f"║" + "YOUR CART".center(52) + "║")
    print("╠════════════════════╦═══════════════════════════════╣")
    print("║      Product       ║             Quantity          ║")
    print("╠════════════════════╬═══════════════════════════════╣")

    for idx, item in enumerate(cart, 1):
        product_name = item["product"].product_name
        quantity = item["quantity"]
        print(f"║   {idx}. {product_name:<13} ║    {quantity:<26} ║")

    print("╚════════════════════╩═══════════════════════════════╝")

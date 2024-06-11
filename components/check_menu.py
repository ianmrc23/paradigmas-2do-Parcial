from multiprocessing.connection import Client
from utils.menu_table import show_checkout, show_shipping_methods
from utils.os_utils import clear_screen, invalid_choice, save_pickle_file, wait_for_key
from schemas.polymorphism import (
    CardPayment,
    CashPayment,
    ExpressShipping,
    InStorePickup,
    QRPayment,
    StandardShipping,
    calculate_shipping,
    process_payment
)


def check_out_menu(client: Client):
    total_amount, total_weight = client.calculate_totals()
    total_products = len(client.cart)
    distance = client.client_distance_from_store

    while True:
        payment_method = select_payment_method(client)
        if not payment_method:
            return

        total_with_discount = process_payment(payment_method, total_amount)

        shipping_method = select_shipping_method(client)
        if shipping_method:
            break

    shipping_cost = calculate_shipping(
        shipping_method, total_weight, distance, total_products)
    total_amount_with_shipping = total_with_discount + shipping_cost

    clear_screen()
    print(f"\n\n[+] Total amount with discount: {total_with_discount:.2f}$")
    print(f"\n\n[+] Shipping cost: {shipping_cost:.2f}$")
    print(
        f"\n\n[+] Total amount with shipping: {total_amount_with_shipping:.2f}$")
    print("\n\n[+] Thank you for shopping in our store! Have a nice day.")

    client.cart.clear()
    save_pickle_file(client, f"{client.client_email}.pickle")
    wait_for_key()


def select_payment_method(client: Client):
    while True:
        clear_screen()
        client.view_cart()
        show_checkout()
        payment_choice = input(
            "\n\n[*] Enter the NUMBER of the payment method you want or 0 to go back: ")

        if payment_choice == '0':
            return None

        elif payment_choice == '1':
            return CashPayment()

        elif payment_choice == '2':
            return CardPayment()

        elif payment_choice == '3':
            return QRPayment()

        else:
            invalid_choice()


def select_shipping_method(client: Client):
    while True:
        clear_screen()
        client.view_cart()
        show_checkout()
        show_shipping_methods()
        shipping_choice = input(
            "\n\n[*] Enter the NUMBER of the shipping method you want or 0 to go back: ")

        if shipping_choice == '0':
            return None

        elif shipping_choice in ('1', '2', '3'):
            if shipping_choice == '1':
                return StandardShipping()

            elif shipping_choice == '2':
                return ExpressShipping()

            elif shipping_choice == '3':
                return InStorePickup()

        else:
            invalid_choice()

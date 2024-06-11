from schemas.client_manager import Client
from utils.os_utils import file_exists, load_pickle_file, save_pickle_file


def login_user():
    client_email = input("\n\n[*] Enter your email: ")
    client_password = input("\n\n[*] Enter your password: ")
    client_file = f"{client_email}.pickle"

    if file_exists(client_file):
        client = load_pickle_file(client_file)

        if client.client_password == client_password:
            print(f"\n\n[+] Welcome back, {client.client_name}!")
            return client

        else:
            print("\n\n[-] Incorrect password.")
            return None

    else:
        print("\n\n[-] No account found with this email.")
        return None


def register_new_user():
    while True:
        try:
            client_id = int(input("\n\n[*] Enter your ID: "))
            if client_id <= 0:
                raise ValueError("\n\n[-] ID must be a positive integer.")
            break
        except ValueError as e:
            print(f"\n\n[-] Error: {e}")
    client_name = input("\n\n[*] Enter your name: ")
    client_email = input("\n\n[*] Enter your email: ")
    client_password = input("\n\n[*] Enter your password: ")
    client_address = input("\n\n[*] Enter your address: ")
    while True:
        try:
            client_distance = float(
                input("\n\n[*] Enter your distance from the store: "))
            if client_distance >= 0:
                break
            else:
                raise ValueError(
                    "\n\n[-] Distance must be a non-negative number.")
        except ValueError as e:
            print(f"\n\n[-] Error: {e}")

    new_client = Client(
        client_id=client_id,
        client_name=client_name,
        client_email=client_email,
        client_password=client_password,
        client_address=client_address,
        client_distance=client_distance
    )
    save_pickle_file(new_client, f"{client_email}.pickle")
    print(f"\n\n[+] User {client_name} has been registered successfully!")
    return new_client

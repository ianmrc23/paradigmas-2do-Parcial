from schemas.client_manager import Client
from utils.os_utils import file_exists, load_pickle_file, save_pickle_file


def login_user():
    """
    Autentica a un usuario mediante su email y contraseña.
    """
    client_email = input("\n\n[*] Enter your email: ")
    client_password = input("\n\n[*] Enter your password: ")
    client_file = f"{client_email}.pickle"

    # Verifica si el archivo del cliente existe
    if file_exists(client_file):
        client = load_pickle_file(client_file)

        # Verifica la contraseña
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
    """
    Registra un nuevo usuario solicitando su información y guardándola en un archivo pickle.
    """
    # Solicita y valida el ID del cliente
    while True:
        try:
            client_id = int(input("\n\n[*] Enter your ID: "))
            if client_id <= 0:
                raise ValueError("\n\n[-] ID must be a positive integer.")
            break
        except ValueError as e:
            print(f"\n\n[-] Error: {e}")

    # Solicita la información del cliente
    client_name = input("\n\n[*] Enter your name: ")
    client_email = input("\n\n[*] Enter your email: ")
    client_password = input("\n\n[*] Enter your password: ")
    client_address = input("\n\n[*] Enter your address: ")

    # Solicita y valida la distancia del cliente a la tienda
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

    # Crea un nuevo objeto Client
    new_client = Client(
        client_id=client_id,
        client_name=client_name,
        client_email=client_email,
        client_password=client_password,
        client_address=client_address,
        client_distance=client_distance
    )
    # Guarda el nuevo cliente en un archivo pickle
    save_pickle_file(new_client, f"{client_email}.pickle")
    print(f"\n\n[+] User {client_name} has been registered successfully!")
    return new_client

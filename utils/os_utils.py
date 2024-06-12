import os
import pickle


def get_main_dir(subdir=""):
    """
    Obtiene el directorio principal del proyecto.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    main_dir = os.path.join(current_dir, "..")
    if subdir:
        return os.path.join(main_dir, subdir)
    return main_dir


def invalid_choice():
    """
    Muestra un mensaje de opción inválida y espera a que el usuario presione una tecla.
    """
    print("\n\n[-] Invalid choice. Please enter a valid option.")
    wait_for_key()


def confirm_choice_input(prompt):
    """
    Solicita al usuario confirmar su elección con 'y' o 'n'.
    """
    while True:
        choice = input(prompt)
        if choice.lower() in ("y", "n"):
            return choice.lower()
        else:
            print("\n\n[-] Invalid choice. Please enter 'y' or 'n'.")


def clear_screen():
    """
    Limpia la pantalla de la consola.
    """
    os.system("cls" if os.name == "nt" else "clear")


def wait_for_key():
    """
    Espera a que el usuario presione la tecla RETURN para continuar.
    """
    input("\n\n[*] Press RETURN to continue ")


def farewell_message():
    """
    Muestra un mensaje de despedida y cierra el programa.
    """
    print("\n\n[+] Thank you for visiting us! We hope to see you again soon!\n\n")
    exit(0)


def save_pickle_file(data, filename):
    """
    Guarda datos en un archivo pickle.
    """
    filepath = get_main_dir(f"db/{filename}")
    with open(filepath, "wb") as file:
        pickle.dump(data, file)


def load_pickle_file(filename):
    """
    Carga datos desde un archivo pickle.
    """
    filepath = get_main_dir(f"db/{filename}")
    with open(filepath, "rb") as file:
        return pickle.load(file)


def file_exists(file_path):
    """
    Verifica si un archivo existe en la ruta especificada.
    """
    return os.path.exists(get_main_dir(f"db/{file_path}"))

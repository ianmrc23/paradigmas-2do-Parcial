import os
import pickle


def get_main_dir(subdir=""):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    main_dir = os.path.join(current_dir, "..")
    if subdir:
        return os.path.join(main_dir, subdir)
    return main_dir


def invalid_choice():
    print("\n\n[-] Invalid choice. Please enter a valid option.")
    wait_for_key()


def confirm_choice_input(prompt):
    while True:
        choice = input(prompt)
        if choice.lower() in ("y", "n"):
            return choice.lower()
        else:
            print("\n\n[-] Invalid choice. Please enter 'y' or 'n'.")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def wait_for_key():
    input("\n\n[*] Press RETURN to continue ")


def farewell_message():
    print("\n\n[+] Thank you for visiting us! We hope to see you again soon!\n\n")
    exit(0)


def save_pickle_file(data, filename):
    filepath = get_main_dir(f"db/{filename}")
    with open(filepath, "wb") as file:
        pickle.dump(data, file)


def load_pickle_file(filename):
    filepath = get_main_dir(f"db/{filename}")
    with open(filepath, "rb") as file:
        return pickle.load(file)


def file_exists(file_path):
    return os.path.exists(get_main_dir(f"db/{file_path}"))

from utils.os_utils import clear_screen, wait_for_key


def welcome_banner():
    """
    Muestra un banner de bienvenida y espera a que el usuario presione una tecla.
    """
    clear_screen()
    banner = """
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
                                                                    
        ████████╗ ██████╗  ████████╗██╗  ██╗███████╗        
        ╚══██╔══╝██╔═══██╗ ╚══██╔══╝██║  ██║██╔════╝
           ██║   ██║   ██║    ██║   ███████║█████╗   
           ██║   ██║   ██║    ██║   ██╔══██║██╔══╝   
           ██║   ╚██████╔╝    ██║   ██║  ██║███████╗
           ╚═╝    ╚═════╝     ╚═╝   ╚═╝  ╚═╝╚══════╝ 
                                                                                    
         ████████╗████████╗ ██████╗ ██████╗ ███████╗   
         ██╔═════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
         ████████╗   ██║   ██║   ██║██████╔╝█████╗  
         ╚═════██║   ██║   ██║   ██║██╔══██╗██╔══╝  
         ████████║   ██║   ╚██████╔╝██║  ██║███████╗
         ╚═══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
    """
    print(banner)
    wait_for_key()


def auth_menu():
    """
    Muestra el menú de autenticación.
    """
    clear_screen()
    print(f"╔{'═' * 52}╗")
    print(f"║" + "AUTH MENU".center(52) + "║")
    print(f"╠{'═' * 52}╣")
    print(f"║" + "   1. Register".ljust(52) + "║")
    print(f"║" + "   2. Login".ljust(52) + "║")
    print(f"║" + "   3. Exit".ljust(52) + "║")
    print(f"╚{'═' * 52}╝")


def show_main_menu():
    """
    Muestra el menú principal.
    """
    clear_screen()
    print(f"╔{'═' * 52}╗")
    print(f"║" + "MAIN MENU".center(52) + "║")
    print(f"╠{'═' * 52}╣")
    print(f"║" + "   1. Add Product".ljust(52) + "║")
    print(f"║" + "   2. My Cart".ljust(52) + "║")
    print(f"║" + "   3. Checkout".ljust(52) + "║")
    print(f"║" + "   4. Profile".ljust(52) + "║")
    print(f"║" + "   5. Exit".ljust(52) + "║")
    print(f"╚{'═' * 52}╝")


def show_cart_menu():
    """
    Muestra el menú del carrito.
    """
    print(f"╔{'═' * 52}╗")
    print(f"║" + "CART MENU".center(52) + "║")
    print(f"╠{'═' * 52}╣")
    print(f"║" + "   1. View Cart".ljust(52) + "║")
    print(f"║" + "   2. Remove Item".ljust(52) + "║")
    print(f"║" + "   3. Clear Cart".ljust(52) + "║")
    print(f"╚{'═' * 52}╝")


def show_checkout():
    """
    Muestra el menú de checkout.
    """
    print(f"╔{'═' * 52}╗")
    print(f"║" + "CHECKOUT MENU".center(52) + "║")
    print(f"╠{'═' * 52}╣")
    print(f"║" + "   1. Pay with Cash".ljust(52) + "║")
    print(f"║" + "   2. Pay with Card (30% discount) ".ljust(52) + "║")
    print(f"║" + "   3. Pay with QR (10% discount)".ljust(52) + "║")
    print(f"╚{'═' * 52}╝")


def show_shipping_methods():
    """
    Muestra los métodos de envío.
    """
    print(f"╔{'═' * 52}╗")
    print(f"║" + "SHIPPING METHODS".center(52) + "║")
    print(f"╠{'═' * 52}╣")
    print(f"║" + "   1. Standard Shipping".ljust(52) + "║")
    print(f"║" + "   2. Express Shipping".ljust(52) + "║")
    print(f"║" + "   3. In-Store Pickup".ljust(52) + "║")
    print(f"╚{'═' * 52}╝")

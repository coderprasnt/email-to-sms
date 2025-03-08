from termcolor import colored

def display_art():
    # ASCII Art for the message
    art = r"""
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║        🛠️ TOOL AVAILABLE FOR PURCHASE 🛠️         ║
    ║                                                  ║
    ║  Contact https://t.me/witchshophub to purchase   ║
    ║                                                  ║
    ║                Available Versions:               ║
    ║                                                  ║
    ║          1. 🌐 Web Version                       ║
    ║          2. 🐍 Python-Based                      ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    """
    # Print the ASCII art with green color
    print(colored(art, 'green'))

if __name__ == "__main__":
    display_art()

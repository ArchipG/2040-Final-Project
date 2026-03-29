# main.py

# Import the core classes needed to start the system
from file_manager import FileManager
from menu import Menu


def main():
    """
    This is the main function where the program starts.

    It initializes the file manager and menu system,
    then launches the main menu loop.
    """

    # Create a FileManager object to handle file operations
    file_manager = FileManager()

    # Create the Menu object and pass the file manager to it
    menu = Menu(file_manager)

    # Start the program by displaying the main menu
    menu.display_main_menu()


# This ensures the program runs only when this file is executed
if __name__ == "__main__":
    main()

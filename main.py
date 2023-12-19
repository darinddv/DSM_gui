
from dsm_builder import get_service_input, update_dsm_json

def display_logo():
    logo = """
 ██████╗ █████╗ ███╗   ██╗███████╗    ██████╗ ███████╗███╗   ███╗
██╔════╝██╔══██╗████╗  ██║██╔════╝    ██╔══██╗██╔════╝████╗ ████║
██║     ███████║██╔██╗ ██║███████╗    ██║  ██║███████╗██╔████╔██║
██║     ██╔══██║██║╚██╗██║╚════██║    ██║  ██║╚════██║██║╚██╔╝██║
╚██████╗██║  ██║██║ ╚████║███████║    ██████╔╝███████║██║ ╚═╝ ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝    ╚═════╝ ╚══════╝╚═╝     ╚═╝                                                              
    """
    print(logo)

# Assuming this function is part of your menu system
# and gets called when the user chooses to build/edit a DSM


def display_main_menu():
    print("1. Load Data")
    print("2. Evaluate Criteria")
    print("3. Display Results")
    print("4. Build New DSM")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def display_dsm_build_menu():
    print("\n--- Build DSM Menu ---")
    print("1. Add New Service")
    print("2. Edit Existing Service")
    print("3. Delete Service")
    print("4. View All Services")
    print("5. Return to Main Menu")
    choice = input("Enter your choice: ")
    return choice


def main():
    while True:
        display_logo()
        choice = display_main_menu()

        if choice == "1":
            # Load data functionality
            pass
        elif choice == "2":
            # Evaluate criteria functionality
            pass
        elif choice == "3":
            # Display results functionality
            pass
        elif choice == "4":
            handle_dsm_build()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def handle_dsm_build():
    while True:
        choice = display_dsm_build_menu()

        if choice == "1":
            # Add new service functionality
            service_directory = "."  # Replace with the desired directory path
            service_name, criteria = get_service_input()
            update_dsm_json(service_name, criteria)
        elif choice == "2":
            # Edit existing service functionality
            pass
        elif choice == "3":
            # Delete service functionality
            pass
        elif choice == "4":
            # View all services functionality
            pass
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

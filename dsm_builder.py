import json
import os

def check_dsm_exists(service_name, directory="."):
    filename = os.path.join(directory, f"{service_name}.json")
    return os.path.exists(filename)

def get_service_input(directory="."):
    while True:
        service_name = input("Enter the service name: ").strip()
        if not service_name:
            print("Service name cannot be blank. Please enter a valid name.")
            continue
        if check_dsm_exists(service_name, directory):
            print(f"A DSM file with the name '{service_name}.json' already exists.")
            continue_option = input("Do you want to continue editing this DSM? (y/n): ")
            if continue_option.lower() != 'y':
                continue
        break

    criteria = []
    while True:
        criterion = input("Enter a criterion (or leave empty to finish): ")
        if criterion:
            criteria.append(criterion)
        else:
            break

    return service_name, criteria


def update_dsm_json(service_name, criteria, directory="."):
    dsm_directory = os.path.join(directory, "DSM_Models")
    if not os.path.exists(dsm_directory):
        os.makedirs(dsm_directory)

    filename = os.path.join(dsm_directory, f"{service_name}.json")
    dsm_data = {"criteria": criteria}

    with open(filename, "w") as file:
        json.dump(dsm_data, file, indent=4)
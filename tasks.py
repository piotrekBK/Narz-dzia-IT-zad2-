import json
import os
# import main

FILE_NAME = 'storage.js'

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return [] 

def save_data(data):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def add_item():
    new_item = input("\nWpisz nazwę elementu do dodania: ")
    data = load_data()
    data.append(new_item + " ❌")
    save_data(data)
    print(f" Dodano: '{new_item}'")

def delete_item():
    data = load_data()
    
    if not data:
        print("\nLista jest pusta. Nie ma nic do usunięcia.")
        return

    print("\n--- Które zadanie chcesz usunąć? ---")
    for index, item in enumerate(data, start=1):
        print(f"{index}. {item}")
    
    choice = input("Podaj numer do usunięcia (lub 'q' aby wyjść): ")
    
    if choice.lower() == 'q':
        return

    try:
        index_to_delete = int(choice) - 1
        if 0 <= index_to_delete < len(data):
            removed_item = data.pop(index_to_delete)
            save_data(data)
            print(f" Usunięto: '{removed_item}'")
        else:
            print(" Błąd: Nie ma elementu o takim numerze.")
    except ValueError:
        print(" Błąd: Musisz podać liczbę.")

def main():
    while True:
        print("\n=== Edytuj ===")
        print("1. Dodaj")
        print("2. Usuń")
        print("3. Wróć")
        
        wybor = input("Wybierz opcję (1/2/3): ")
        
        if wybor == '1':
            add_item()
        elif wybor == '2':
            delete_item()
        elif wybor == '3':
            break
        else:
            print(" Nieznana opcja. Wybierz 1, 2 lub 3.")

if __name__ == '__main__':
    main()
import json
import os
import tasks 

FILE_NAME = 'storage.js'
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
        
def show_list():
    lista = load_data()
    
    if not lista:
        print("\nLista jest pusta.")
        return

    print("\n--- lista ---")
    for index, item in enumerate(lista, start=1):
        print(f"{index}. {item}")
    print('-------------')

def lista_choice():
    while True:
        show_list()
        list_choice = input('1. Odchacz\n2. Edytuj\n3. Wróć\nWybierz opcję (1/2/3): ')

        if list_choice == '1':
            if list_choice == '1':
                try:
                    index = int(input("Podaj numer zadania do odhaczenia: "))
                    odchacz(index)
                except ValueError:
                    print("To nie jest liczba!")
        elif list_choice == '2':
            tasks.main()
        elif list_choice == '3':
            break
        else:
            print("Nie ma takiego wyboru")

def odchacz(index):
    lista = load_data()

    i = index - 1

    if 0 <= i < len(lista):
        lista[i] = lista[i].replace("❌", "✔️")
        save_data(lista)
        print("Zadanie odhaczone!")
    else:
        print("Zły indeks!")

def save_data(data):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def main():
    while True:
        choice = input('----------------\n1. Wyświetl listę\n2. Wyjdź\nWybierz opcję (1/2): ')

        if choice == '1':
            lista_choice()
        elif choice == '2':
            break
        else:
            print("Nie ma takiego wyboru")
            
main()
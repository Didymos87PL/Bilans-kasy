import csv
import os

def load_transactions(file_path):
    transactions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pominięcie nagłówka
        for row in reader:
            transactions.append(row)
    return transactions

def save_transactions(initial_balance, transactions, final_balance, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Nr Transakcji", "Typ", "Kwota", "Opis", "Saldo Po Transakcji"])
        writer.writerow([1, "Saldo Początkowe", initial_balance, "", initial_balance])
        current_balance = initial_balance
        transaction_number = 2
        for transaction in transactions:
            if transaction[0] == "Przychód":
                current_balance += float(transaction[1])
            else:
                current_balance -= float(transaction[1])
            writer.writerow([transaction_number] + transaction + [current_balance])
            transaction_number += 1
        writer.writerow([transaction_number, "Saldo Końcowe", final_balance, "", final_balance])

def manage_budget():
    print("Witaj w programie do zarządzania budżetem!")

    file_path = os.path.join("C:\\", "Users", "didym", "Desktop", "Programy do pracy", "transactions_history.csv") # tu ustawiasz swoją ściężkę do zapisania pliku.
    
    while True:
        print("\n1: Wprowadź dane")
        print("2: Odczytaj dane z pliku")
        print("3: Zakończ")
        choice = input("Wybierz opcję (1, 2 lub 3): ")

        if choice == '3':
            print("Zakończenie pracy programu.")
            break

        transactions = []

        if choice == '2':
            if os.path.exists(file_path):
                transactions = load_transactions(file_path)
                for transaction in transactions:
                    print(transaction)
                continue
            else:
                print("Plik nie istnieje. Przechodzę do wprowadzania danych.")

        print("Możesz używać liczb z kropką (.) jako separatora dziesiętnego.")
        print("Spacje są dozwolone i będą ignorowane.")

        initial_balance = input("Podaj saldo początkowe: ").replace(',', '.').replace(' ', '')
        initial_balance = float(initial_balance)
        current_balance = initial_balance

        while True:
            print("\n1: Dodaj Przychód")
            print("2: Dodaj Wydatek")
            print("3: Zakończ i Zapisz")
            user_choice = input("Wybierz opcję (1, 2 lub 3): ")

            if user_choice == '3':
                print("Zapisywanie danych i powrót do głównego menu.")
                break
            elif user_choice not in ['1', '2']:
                print("Nieprawidłowy wybór. Wybierz 1, 2 lub 3.")
                continue

            amount = input("Podaj kwotę: ").replace(',', '.').replace(' ', '')
            amount = float(amount)

            if user_choice == '1':  # Przychód
                source = input("Podaj tytuł przychodu: ")
                current_balance += amount
                transactions.append(["Przychód", amount, source])

            elif user_choice == '2':  # Wydatek
                description = input("Podaj tytuł wydatku: ")
                current_balance -= amount
                transactions.append(["Wydatek", amount, description])

            print(f"Aktualne saldo: {current_balance}")

        save_transactions(initial_balance, transactions, current_balance, file_path)
        print(f"Historia transakcji została zapisana w pliku '{file_path}'.")

# Uruchomienie programu
manage_budget()

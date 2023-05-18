class SymbolTableEntry:
    def __init__(self, token_id, name, data_type):
        self.token_id = token_id
        self.name = name
        self.data_type = data_type


class SymbolTable:
    def __init__(self):
        self.entries = []

    def insert(self, token_id, name, data_type):
        entry = SymbolTableEntry(token_id, name, data_type)
        self.entries.append(entry)
        print("Entry inserted successfully.")

    def update(self, token_id, name, data_type):
        for entry in self.entries:
            if entry.token_id == token_id:
                entry.name = name
                entry.data_type = data_type
                print("Entry updated successfully.")
                return
        print("Entry not found.")

    def search(self, token_id):
        for entry in self.entries:
            if entry.token_id == token_id:
                print("Entry found:")
                print("Token ID:", entry.token_id)
                print("Name:", entry.name)
                print("Data Type:", entry.data_type)
                return
        print("Entry not found.")

    def delete(self, token_id):
        for entry in self.entries:
            if entry.token_id == token_id:
                self.entries.remove(entry)
                print("Entry deleted successfully.")
                return
        print("Entry not found.")


def main():
    symbol_table = SymbolTable()

    while True:
        print("\n--- Symbol Table Management ---")
        print("1. Insert Entry")
        print("2. Update Entry")
        print("3. Search Entry")
        print("4. Delete Entry")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            token_id = int(input("Enter Token ID: "))
            name = input("Enter Name: ")
            data_type = input("Enter Data Type: ")
            symbol_table.insert(token_id, name, data_type)
        elif choice == "2":
            token_id = int(input("Enter Token ID: "))
            name = input("Enter New Name: ")
            data_type = input("Enter New Data Type: ")
            symbol_table.update(token_id, name, data_type)
        elif choice == "3":
            token_id = int(input("Enter Token ID: "))
            symbol_table.search(token_id)
        elif choice == "4":
            token_id = int(input("Enter Token ID: "))
            symbol_table.delete(token_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

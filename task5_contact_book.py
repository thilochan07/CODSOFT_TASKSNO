"""
Task 5: Contact Book Application
CodSoft Python Programming Internship
Author: Thilochan P
"""

import json
import os

DATA_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def display_menu():
    print("\n===============================")
    print("      CONTACT BOOK MANAGER     ")
    print("===============================")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact Details")
    print("5. Delete Contact")
    print("6. Exit")
    print("===============================")

def add_contact(contacts):
    print("\n--- ADD NEW CONTACT ---")
    name = input("Enter Name*: ").strip()
    if not name:
        print("[!] Name is mandatory.")
        return
    phone = input("Enter Phone Number*: ").strip()
    if not phone:
        print("[!] Phone number is mandatory.")
        return
    email = input("Enter Email Address: ").strip()
    address = input("Enter Address: ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print(f"[✓] Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("\n[!] No contacts found.")
        return
    print("\n--- CONTACT LIST ---")
    print(f"{'S.No':<6}{'Name':<22}{'Phone Number':<18}")
    print("-" * 46)
    for idx, c in enumerate(contacts, 1):
        print(f"{idx:<6}{c['name']:<22}{c['phone']:<18}")

def search_contact(contacts):
    if not contacts:
        print("\n[!] Contact book is empty.")
        return
    query = input("\nEnter Name or Phone Number to search: ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone'].lower()]

    if not results:
        print("[!] No matching contacts found.")
        return

    print(f"\nFound {len(results)} match(es):")
    for c in results:
        print("-" * 40)
        print(f"Name   : {c['name']}")
        print(f"Phone  : {c['phone']}")
        print(f"Email  : {c.get('email', 'N/A')}")
        print(f"Address: {c.get('address', 'N/A')}")
    print("-" * 40)

def update_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("\nEnter contact number to update: ")) - 1
        if 0 <= idx < len(contacts):
            c = contacts[idx]
            print(f"Updating '{c['name']}' (Press Enter to keep current value):")
            
            new_name = input(f"New Name [{c['name']}]: ").strip()
            new_phone = input(f"New Phone [{c['phone']}]: ").strip()
            new_email = input(f"New Email [{c.get('email', '')}]: ").strip()
            new_address = input(f"New Address [{c.get('address', '')}]: ").strip()

            if new_name: c['name'] = new_name
            if new_phone: c['phone'] = new_phone
            if new_email: c['email'] = new_email
            if new_address: c['address'] = new_address

            save_contacts(contacts)
            print("[✓] Contact updated successfully!")
        else:
            print("[!] Invalid contact number.")
    except ValueError:
        print("[!] Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("\nEnter contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            deleted = contacts.pop(idx)
            save_contacts(contacts)
            print(f"[✓] Contact '{deleted['name']}' deleted successfully!")
        else:
            print("[!] Invalid contact number.")
    except ValueError:
        print("[!] Please enter a valid number.")

def main():
    contacts = load_contacts()
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("\nThank you for using Contact Book! Goodbye! 👋")
            break
        else:
            print("[!] Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    main()

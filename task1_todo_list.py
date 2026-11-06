"""
Task 1: To-Do List Application
CodSoft Python Programming Internship
Author: Thilochan P
"""

import json
import os

DATA_FILE = "todo_tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def display_menu():
    print("\n===============================")
    print("      TO-DO LIST MANAGER       ")
    print("===============================")
    print("1. View All Tasks")
    print("2. Add New Task")
    print("3. Mark Task as Completed")
    print("4. Update Task Description")
    print("5. Delete Task")
    print("6. Exit")
    print("===============================")

def view_tasks(tasks):
    if not tasks:
        print("\n[!] No tasks found in your list.")
        return
    print("\n--- YOUR TASKS ---")
    for idx, task in enumerate(tasks, 1):
        status = "[✓] Done" if task["completed"] else "[ ] Pending"
        priority = f"[{task.get('priority', 'Medium')}]"
        print(f"{idx}. {status} {priority} {task['title']}")

def add_task(tasks):
    title = input("\nEnter task description: ").strip()
    if not title:
        print("[!] Task description cannot be empty.")
        return
    print("Select Priority: 1. High | 2. Medium | 3. Low")
    p_choice = input("Choice (default 2): ").strip()
    priority_map = {"1": "High", "2": "Medium", "3": "Low"}
    priority = priority_map.get(p_choice, "Medium")
    
    tasks.append({"title": title, "completed": False, "priority": priority})
    save_tasks(tasks)
    print(f"[✓] Task '{title}' added successfully!")

def mark_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("\nEnter task number to mark as completed: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["completed"] = True
            save_tasks(tasks)
            print(f"[✓] Task '{tasks[idx]['title']}' marked as completed!")
        else:
            print("[!] Invalid task number.")
    except ValueError:
        print("[!] Please enter a valid number.")

def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("\nEnter task number to update: ")) - 1
        if 0 <= idx < len(tasks):
            new_title = input(f"Enter new description for '{tasks[idx]['title']}': ").strip()
            if new_title:
                tasks[idx]["title"] = new_title
                save_tasks(tasks)
                print("[✓] Task updated successfully!")
            else:
                print("[!] Task description cannot be empty.")
        else:
            print("[!] Invalid task number.")
    except ValueError:
        print("[!] Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"[✓] Task '{removed['title']}' deleted successfully!")
        else:
            print("[!] Invalid task number.")
    except ValueError:
        print("[!] Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("\nThank you for using To-Do List Manager! Goodbye! 👋")
            break
        else:
            print("[!] Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    main()

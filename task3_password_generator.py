"""
Task 3: Random Password Generator
CodSoft Python Programming Internship
Author: Thilochan P
"""

import random
import string

def generate_password(length, use_uppercase, use_digits, use_symbols):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one character type must be selected.")

    # Guarantee at least one character from each selected category
    password = []
    password.append(random.choice(string.ascii_lowercase))
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill remaining length
    while len(password) < length:
        password.append(random.choice(chars))

    random.shuffle(password)
    return "".join(password)

def calculate_strength(length, use_upper, use_digits, use_symbols):
    score = 0
    if length >= 12: score += 2
    elif length >= 8: score += 1
    if use_upper: score += 1
    if use_digits: score += 1
    if use_symbols: score += 1

    if score <= 2: return "Weak 🔴"
    elif score <= 4: return "Moderate 🟡"
    else: return "Strong 🟢"

def main():
    print("========================================")
    print("      RANDOM PASSWORD GENERATOR        ")
    print("========================================")

    while True:
        try:
            length = int(input("\nEnter desired password length (min 4): "))
            if length < 4:
                print("[!] Password length should be at least 4 for security.")
                continue
            break
        except ValueError:
            print("[!] Please enter a valid integer.")

    print("\nPassword Configuration Options:")
    use_upper = input("Include uppercase letters? (y/n, default y): ").strip().lower() != 'n'
    use_digits = input("Include numbers? (y/n, default y): ").strip().lower() != 'n'
    use_symbols = input("Include special symbols? (y/n, default y): ").strip().lower() != 'n'

    try:
        pwd = generate_password(length, use_upper, use_digits, use_symbols)
        strength = calculate_strength(length, use_upper, use_digits, use_symbols)
        print("\n----------------------------------------")
        print(f"Generated Password : {pwd}")
        print(f"Password Strength  : {strength}")
        print("----------------------------------------")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()

import re

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("❌ Use at least 8 characters")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("❌ Add lowercase letters")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("❌ Add uppercase letters")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("❌ Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("❌ Add special characters")

    print("\n🔍 Analyzing password...")
    if strength == 5:
        print("✅ Your password is Strong!")
    elif strength >= 3:
        print("🟡 Your password is Moderate.")
    else:
        print("🔴 Your password is Weak.")

    if remarks:
        print("\nSuggestions to improve:")
        for remark in remarks:
            print(remark)

# Run the checker
user_password = input("Enter a password to check: ")
check_password_strength(user_password)

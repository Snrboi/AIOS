line = "=" * 40

# Welcome Section
print(line)
print("   WELCOME TO DEVELOPER OS")
print("Current Version: v 0.4.0")
print(line)

# Data Collection Section
name = input("Enter Name: ").title().strip()
age = int(input("Enter Age: "))
location = input("Your location: ").strip()
current_program = input("What program are you currently learning? ").title().strip()
dream_career = input("What is your dream profession? ").title().strip()
github = input("What is your Github username? ").strip().lower()
favourite_club = input("What is your Favourite football club? ").strip().lower()

# Welcome Page
print(line)
print("      PROFILE")
print(f"Welcome, {name}!")
print(line)
# Role Validation
print(line)
print("     Role")
print(line)
print(line)
if age >= 18:
    if github == "snrboi":
        print("Role: Lead AI Engineer")
    else:
        print("Role: Community Developer")
else:
    print("Role: AI Student")
print(line)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Location: {location}".title())
print(f"Current Program: {current_program}")
print(f"Dream Career: {dream_career}")
print(f"Github: {github}")
print(f"Favourite Club: {favourite_club}".title())

# Validation Section
print(line)
print("  PROFILE VALIDATION")
print(line)
print(f"Adult: {age >= 18}")
print(f"Chelsea Fan: {favourite_club == 'chelsea'}")
print(f"Github Username Matches: {github == 'snrboi'}")

# Personalized messages Section
print(line)
print("    PERSONALIZED MESSAGES")
print(line)
# github and age validation
if age >= 18:
    if github == "snrboi":
        print("Role: Lead AI Engineer")
    else:
        print("Role: Community Developer")
else:
    print("Role: AI Student")

# football club and age validation
if favourite_club == "chelsea":
    if age >= 18:
        print("Premium Chelsea Member")
    else:
        print("Junior Chelsea Member")
else:
    print("Welcome, football fan!")

# log in validation
logged_in = True

if logged_in:
    print("Session Active")
else:
    print("Please login")


# Utilities Section
print(line)
print("  LOADING DEVELOPER UTILITIES.....")
print(line)

# Calculator
print(line)
print("  SIMPLE CALCULATOR")
print(line)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Quotient: {a / b}")
print(f"Remainder: {a % b}")
print(f"Power: {a ** b}")

# Goodbye section
print(line)
print("Thank you for using DeveloperOS!")
print("Version: v0.4.0")
print(line)

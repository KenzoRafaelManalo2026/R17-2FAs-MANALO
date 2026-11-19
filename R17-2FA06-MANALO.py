# Version 2: Added String Formatting
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
favorite_subject = input("Enter favorite subject: ").strip()

full_name = f"{first_name} {last_name}".title()
full_name_capitalized = full_name.upper()
section_upper = section.upper()
subject_proper = favorite_subject.title()

char_count = len(full_name)

print("\nFormatted Output:")
print(f"Name: {full_name}")
print(f"Name Code: {full_name_capitalized}")
print(f"Section: {section_upper}")
print(f"Favorite Subject: {subject_proper}")
print(f"Character Count: {char_count}")

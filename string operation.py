text=input("Enter a string: ")

print("1. Lowercase: ",text.lower())

print("2. Uppercase: ",text.upper())

print("3. Length: ",len(text))

print("4. Capitalization: ",text.capitalize())

print("5. Replace: ",text.replace("python", "html"))

print("6. Title: ",text.title())

print("7. Split: ",text.split())

words=["Html", "is", "fun"]
print("8. Join: ", " ".join(words))

print("9. Starts with: ", text.startswith("Hello"))

print("10. Ends with: ", text.endswith("World"))

print("11. Find: ", text.find("World"))

print("12. Count: ", text.count("1"))

print("13. Isalpha: ", "Hello".isalpha())

print("14. Reverse: ", text[::-1])
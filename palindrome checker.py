text=input("Enter a word: ")

text=text.lower()

text=text.replace(" ", "")

reversedtext=""

reversedtext=text[::-1]

if text==reversedtext:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
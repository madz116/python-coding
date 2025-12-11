sentence=str(input("Enter a sentence: ")).lower()
letter=str(input("Enter the letter you want to find: ")).lower()
count=0
for i in sentence:
    if i==letter:
        count=count+1
print("Total: ",count)
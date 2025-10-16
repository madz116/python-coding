amount=int(input("Enter the amount of money: "))

note=amount // 100
print("100 Dollar notes: ",note)
amount=amount % 100

note=amount // 50
print("50 Dollar notes: ",note)
amount=amount % 50

note=amount // 20
print("20 Dollar notes: ",note)
amount=amount % 20

note=amount // 10
print("10 Dollar notes: ",note)
amount=amount % 10

note=amount // 5
print("5 Dollar notes: ",note)
amount=amount % 5

note=amount // 2
print("2 Dollar notes: ",note)
amount=amount % 2

note=amount // 1
print("1 Dollar notes: ",note)
amount=amount % 1
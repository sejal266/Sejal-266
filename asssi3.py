# calculator using if else

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

print("Choose operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
 
choice = int(input("Enter your choice (1/2/3/4): "))

if choice == 1:
     result = num1 + num2
elif choice == 2:
     result = num1 - num2
elif choice == 3:
     result = num1 * num2
elif choice == 4:
     if num2 != 0:
         result = num1 // num2  # Integer division
     else:
         result = "Cannot divide by zero!"
else:
     result = "Invalid choice"

print("Result:", result)
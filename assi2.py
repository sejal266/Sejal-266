#Simple Marriage Eligibility Checker with Gender
for i in range(1, 4):
     gender = input("Enter your gender (male/female): ").lower()
     age = int(input("Enter your age: "))

     if gender == "male" and age >= 21:
         print("You are eligible for marriage!")
         break
     elif gender == "female" and age >= 18:
         print("You are eligible for marriage!")
         break
     else:
         print(" You are not eligible for marriage yet. Try again later.\n")

else:
     print("you are not worthy of marriage")
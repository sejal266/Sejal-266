# Take inputs
bill_amount = int(input("Enter total bill amount: "))
num_friends = int(input("Enter number of friends: "))

# Split the bill
if num_friends > 0:
    split_amount = bill_amount // num_friends
    print("Each person pays:", split_amount)
else:
    print("Number of friends must be greater than 0")

# Tip calculation
print("\nTip suggestions:")
for tip_percent in range(10, 51, 10):  # 10%, 20%, ..., 50%
    tip = (bill_amount * tip_percent) // 100
    print(f"{tip_percent}% tip = {tip}")
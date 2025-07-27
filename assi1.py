#Bottles drinked per day
total_bottles = 100 
daily_use = int(input("Enter bottles you drink per day:"))
day = 1

while total_bottles > 0:
    drimk = min(daily_use,total_bottles)
    total_bottles -=drink

    if total_bottles == 0:
        print(f"Day {day}: Drank {drink} bottles. 0 left.")
        print("Please refill the bottles!")
    elif 40 <= total_bottles <= 50:
        print(f"Day {day}: Drank {drink} bottles.only 40 to 50 left.")
    else:
        print(f"Day {day: Drank {drink} bottles.{total_bottles} left.")
              
              day+=
ID = 5
rate = 0.4
day = 0

while ID < 91:
    ID = ID * (1 + rate) 
    ID = ID - ID % 1 
    day += 1
    print(f"Day: {day}, ID: {ID}")

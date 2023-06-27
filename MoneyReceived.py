def total_amount():
    total = int(input("How many 100s: "))*100 
    total += int(input("How many 50s: "))*50 
    total += int(input("How many 20s: "))*20 
    total += int(input("How many 10s: "))*10 
    return total
    
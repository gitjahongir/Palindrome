def number(a): #create a function
    if a.isnumeric(): #check if var is numeric
        if a == a[::-1]:
            return f"Palindrom son!,{a}"
        elif a != a[::-1]:
            return "Palindrom son emas..."
    elif a.isalpha(): #check if var is string
        if a == a[::-1]:
            return f"Palindrom matn!,{a}"
        elif a != a[::-1]:
            return "Palindrom matn emas..."
    elif a.isalnum(): #check if var is both string and number
        if a == a[::-1]:
            return f"Palindrom algebraik son!:{a}"
        elif a != a[::-1]:
            return "Palindrom algebraik son emas..."
print(number(input("Son kiriting:"))) #print function

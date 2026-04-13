try:
    data = input().split()
    if len(data) != 2:
        print("Error: Invalid input")
    else:
        a = int(data[0])
        b = int(data[1])
        result = a / b
        print(result)

except ValueError:
    print("Error: Invalid input")
except ZeroDivisionError:
    print("Error: Division by zero")

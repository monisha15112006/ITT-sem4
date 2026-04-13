a =int(input("Enter side 1:"));
b = int(input("Enter side 2:"));
c = int(input("Enter side 3:"));
if a + b > c and a + c > b and b + c > a:
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")

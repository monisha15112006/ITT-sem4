c=int(input("Enter temperature in celcius:"))
if(c<=100 and c>=-50):
   f=(c*(9/5))+32
   print("Temperature in fahrenheit",f)
else:
   print("Invalid input")

p=int(input("Enter principle amount:"))
r=int(input("Enter rate of interest:"))
t=int(input("Enter time period:"));
if(p<=100000 and 1<=p and 1<=r and r<=20 and 1<=t and t<=10):
   si=(p*r*t)/100;
   print("Simple interest:",si);
else:
   print("Invalid input");


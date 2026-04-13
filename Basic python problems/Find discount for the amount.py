amount = float(input("Enter your bill amount:"));
if amount>=5000:
   amount=amount*0.2;
   print("You have recieved 20% discount, and your final bill is : Rs.",amount);
elif amount>=3000:
   amount=amount*0.1;
   print("You have recieved 10% discount , and your final bill is :Rs.",amount);
else:
   print("You have recieved no discount, your final bill amount is :Rs.",amount);

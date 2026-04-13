sal=int(input("Enter basic salary:"));
if(sal<=50000 and 5000<=sal):
   hra=0.2*sal;
   da=0.1*sal;
   gross=sal+hra+da;
   print("Gross salary:",gross);
else:
   print("Invalid salary:");

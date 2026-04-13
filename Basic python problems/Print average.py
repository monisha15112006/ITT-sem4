m1=int(input("Enter first mark:"));
m2=int(input("Enter second mark:"));
m3=int(input("Enter third mark:"));
if(m1<=100 and 0<=m1 and m2<=100 and 0<=m2 and m3<=100 and 0<=m3):
   tot=m1+m2+m3;
   print("Total marks:",tot);
   print("Average:",tot/3);
else:
   print("Invaild mark");

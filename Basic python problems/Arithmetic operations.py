a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
operator=input("Enter operator:")
match operator:
   case "+":
      res=a+b
   case "-":
      res=a-b
   case "*":
      res=a*b
   case "/":
      if(b !=0):
         res=a/b
      else:
         res=-1
   case _:
      res=-1
print(res)

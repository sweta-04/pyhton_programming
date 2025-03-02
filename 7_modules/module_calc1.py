from module_calc import add,sub,mul,div

x,y = map(int,input("Enter two numbers ").split(' '))

print("Addition is " , add(x,y))
print("Substraction is ",sub(x,y))
print("Multiplicaion is ",mul(x,y))
print("Division is ",div(x,y))

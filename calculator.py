def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    try:
        a/b
    except:
        ZeroDivisionError
        print("Zero Division Error!")
def main():
    num1=int(input("Enter your 1st Number:"))
    print("Select your Opreator:")
    choice=input("Enter your Choice:(\nFor Sum:+\nFor Sub:-\nFor Multiply:*\nFor Divison:/)")
    num2=int(input("Enter your 2nd Number:"))
    if choice == '+':
        print(num1,'+',num2,'=',add(num1,num2))
    elif choice == '-':
        print(num1,'-',num2,'=',sub(num1,num2))
    elif choice == '*':
        print(num1,'*',num2,'=',multiply(num1,num2))
    elif choice == '/':
        print(num1,'/',num2,'=',division(num1,num2))
    else:
        print("Invalid input!")

main()
print("CALCULATOR")
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            add=num1+num2;
            print("the sum of given numbers is: ",add)

        elif choice == '2':
            sub=num1-num2;
            print("the subtraction of given numbers is: ",sub)

        elif choice == '3':
            mul=num1*num2;
            print("the product of given numbers is: ",mul)

        elif choice == '4':
            if num2 == 0:
                print('CANNOT DIVIDE BY 0 ')
            else:
                div=num1/num2;
                print("the division of given numbers is: ",div)
else: 
    print("Invalid input")

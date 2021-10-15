def calculator(number1,number2,operator):
    """this function will use the values the user inputs and calculates it depending on what operation they chose"""
    if operator == '+' :
        return number1 + number2
    elif operator == '-' :
        return number1 - number2
    elif operator == '*' :
        return number1 * number2
    elif operator == '//' :
        if number2 == 0:
            return
        else:
            return float(number1)//float(number2)
    elif operator == '/' :
        return (float(number1)/float(number2))
    elif operator == '**' :
        return number1 ** number2
    else:
        return

def parse_input(input_num1,input_num2,input_operator):
    """this function will take the input from the user and call the calculator function and then print out the answer"""
    number1 = input_num1
    number2 = input_num2
    operator = input_operator
    print("Enter Equation: " + str(number1) + " " + (operator) + " " + str(number2))
    print(calculator(number1,number2,operator))
    #this will call the calculator function to print out the answer

parse_input(1,1,'+')
parse_input(10,11,'+')
parse_input(5,2,'//')
parse_input(5.5,3,'/')
parse_input(2.2,5.1,'*')
parse_input(10,2,'**')
parse_input(12,4.2,'*')
parse_input(10,0,"//")

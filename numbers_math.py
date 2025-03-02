
def maths(first_number, operation, second_number):   
    if operation == "+":  
        return first_number + second_number  
    elif operation == "-":  
        return first_number - second_number  
    elif operation == "*":  
        return first_number * second_number  
    elif operation == "/":  
        if second_number != 0:  
            return first_number / second_number  
        else:  
            return "Error: Division by zero is not allowed"  
    else:  
        return "Error: Invalid operation"  

# Example usage
num1 = float(input("Enter first number: "))  
op = input("Enter operation (+, -, *, /): ")  
num2 = float(input("Enter second number: "))  

result = maths(num1, op, num2)  
print("Result:", result)


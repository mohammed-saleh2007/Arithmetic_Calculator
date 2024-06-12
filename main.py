import math

def main():
    while True:
        userinput = input("> ")
        if userinput == "": main()
        if userinput.lower() == "exit":
            print("Good Bye")
            break
        else:
            result = calc(userinput)
            print(result)

def power(base, exponent):
    result = 1
    exponent = int(exponent)
    for _ in range(exponent):
        result *= base
    return result

def root(base, exponent):
    return math.pow(base, 1/exponent)

def calc(user_input):
    array = []
    number = ""
    operation = ""
    
    # check if input is legal
    legal_list = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "p", "P", "i", "R", "(", ")", "s", "n", "c", "o", "t", "a", "+", "-", "*", "/", "^", "e", "x"]
    for i in user_input:
        if i not in legal_list:
            print("illegal input detected!\nStop all operations")
            print(i, "illegal")
            main()

    for i in user_input:
        if i.isdigit() or i == ".":
            if operation:
                array.append(operation)
                operation = ""
            number += i
        else:
            if number:
                array.append(float(number))
                number = ""
            if i == "+" or i == "-" or i == "*" or i == "/":
                if operation:
                    array.append(operation)
                    operation = ""
                array.append(i)
            elif i != " ":
                operation += i    
    if number:
        array.append(float(number))
    
    if operation:
        array.append(operation)
    
    # print("[DEBUGGING] Initial array:", array)

    # replace pi
    index = 0
    while index < len(array):
        if array[index] == "pi":
            product = 3.14159265358979323846
            array[index] = product
        else:
            index += 1

    # calc power and root
    index = 0
    while index < len(array):
        if array[index] == "^" or array[index] == "P":
            num1 = array[index - 1]
            num2 = array[index + 1]
            product = power(num1, num2)
            array[index - 1] = product
            del array[index:index + 2] 

        elif array[index] == "R":
            num2 = array[index - 1]
            num1 = array[index + 1]
            product = root(num1, num2)
            array[index - 1] = product
            del array[index:index + 2] 

        else:
            index += 1

    # calc sin, cos and tan
    index = 0
    while index < len(array):
        if array[index] == "sin(":
            angle = array[index + 1]
            product = math.sin(math.radians(angle))
            array[index] = product
            del array[index+1:index + 3] 
        if array[index] == "cos(":
            angle = array[index + 1]
            product = math.cos(math.radians(angle))
            array[index] = product
            del array[index+1:index + 3] 
        if array[index] == "tan(":
            angle = array[index + 1]
            product = math.tan(math.radians(angle))
            array[index] = product
            del array[index+1:index + 3] 
        else:
            index += 1

    # clac * and /
    index = 0
    while index < len(array):
        if array[index] == "*":
            num1 = array[index - 1]
            num2 = array[index + 1]
            product = num1 * num2

            array[index - 1] = product
            del array[index:index + 2] 

        elif array[index] == "/":
            num1 = array[index - 1]
            num2 = array[index + 1]
            if num2 == 0:
                return "Error: Division by zero"
            product = num1 / num2

            array[index - 1] = product
            del array[index:index + 2] 
        else:
            index += 1
    # calc + and -
    index = 0
    while index < len(array):
        if array[index] == "+":
            num1 = array[index - 1]
            num2 = array[index + 1]
            product = num1 + num2

            array[index - 1] = product
            del array[index:index + 2] 

        elif array[index] == "-":
            num1 = array[index - 1]
            num2 = array[index + 1]
            product = num1 - num2

            array[index - 1] = product
            del array[index:index + 2] 
        else:
            index += 1

    return array[0]

print("\nBasic Arithmetic Calculator\nHow to use?")
print("1. Type 'exit' to quit")
print("2. Type the operation like (5+7/5*6)")
print("3. to get root of number use number R number (ex: 2 R 25 = 5)")
print("4. to get power pf number use number [P or ^] number (ex: 5 P 2 or 5^2 = 25)")
print("CATION: nigative values for R or P may make problems avoid this calculator for this")
print("5. now you can use sin(), cos(), tan() in operation like: 5+sin(30)*cos(45)")
print("6. you can now use pi (ex: 2 * pi * 7)")

main()

import math

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
            if i != " ":
                operation += i
    
    if number:
        array.append(float(number))
    
    if operation:
        array.append(operation)
    
    print("[DEBUGGING] Initial array:", array)

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

while True:
    userinput = input("> ")
    if userinput.lower() == "exit":
        print("Good Bye")
        break
    else:
        result = calc(userinput)
        print("Result:", result)

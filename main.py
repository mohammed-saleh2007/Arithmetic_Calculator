def calc(user_input):
    array = []
    number = ""

    for i in user_input:
        if i.isdigit() or i == ".":
            number += i
        else:
            if number:
                array.append(float(number))
                number = ""
            if i != "=":
                array.append(i)
    
    if number:
        array.append(float(number))
    
    print("[DEBUGGING] Initial array:", array)

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

while True:
    userinput = input("> ")
    if userinput.lower() == "exit":
        print("Good Bye")
        break
    else:
        result = calc(userinput)
        print("Result:", result)

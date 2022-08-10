"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# input_string = input()


"""
first open the file

in order to read the file, you have to use a for loop and the while loop should go inside the for loop
we need to use the rstrip to get rid of the white spaces

make sure to close the file at the end
"""


file_name = open("data.txt")

for i in file_name:
    i = i.rstrip()

    input_string_split = i.split(" ")
    # ['add', '4', '5']
    while True:

        if input_string_split[0] == "add":
            print(add(float(input_string_split[1]), float(input_string_split[2])))
            break

        elif input_string_split[0] == "subtract":
            print(subtract(float(input_string_split[1]), float(input_string_split[2])))
            break


        elif input_string_split[0] == "multiply":
            print(multiply(float(input_string_split[1]), float(input_string_split[2])))
            break


        elif input_string_split[0] == "divide":
            print(divide(float(input_string_split[1]), float(input_string_split[2])))
            break
            
        elif input_string_split[0] == "square":
            print(square(float(input_string_split[1])))
            break

        elif input_string_split[0] == "cube":
            print(cube(float(input_string_split[1])))
            break

        elif input_string_split[0] == "pow":
            print(pow(float(input_string_split[1]), float(input_string_split[2])))
            break

        elif input_string_split[0] == "mod":
            print(mod(float(input_string_split[1]), float(input_string_split[2])))
            break

file_name.close()

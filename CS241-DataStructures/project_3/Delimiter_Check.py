import sys
from Stack import Stack

def delimiter_check(filename):
    file = open(filename)
    holder = Stack() #Store the open delimiters

    for i in list(file.read()):
        if i == '[' or i == '(' or i == '{':
            holder.push(i) #Push it if open delimiter.

        elif i == ']' or i == ')' or i == '}':
            if len(holder) == 0: #If it's closing and there's an empty stack.
                return False
            if len(holder) > 0:
                check = holder.pop() + str(i) #Should match, if not, it's false.
                if check != '()' and check != '[]' and check != '{}':
                    return False

    if len(holder) == 0:#Ran through everything and no errors.
        return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python Delimiter_Check.py file_to_check.py')
    else:
        if delimiter_check(sys.argv[1]):
            print('The file contains balanced delimiters.')
        else:
            print('The file contains IMBALANCED DELIMITERS.')

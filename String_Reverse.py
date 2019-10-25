# Hey fellow warriors   returns Hey wollef sroirraw

# Python3 program to print reverse of all words with letter count more than 5


def print_reverse(s):
    # Taking all the words in a list
    l = [s for s in s.split(' ')]

    for i in range(0, len(l)):
        # printing middle words reversed
        if len(l[i]) > 4:
            print(l[i][::-1], end=' ')
        else:
            print(l[i], end=' ')


string = input("Please enter your string: ")
print_reverse(string)

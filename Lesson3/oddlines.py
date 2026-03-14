file = open("numbers.txt", "r")

for line in file:
    num = int(line.strip())   # convert string to integer
    if num % 2 != 0:          # check odd number
        print(num)

file.close()

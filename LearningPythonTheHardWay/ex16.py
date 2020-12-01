from sys import argv

script, file_name = argv

print(f"We're going to erase file {file_name}")
print("If you don't want to continue, press <Ctrl + C>")
print("if you do want that , hit RETURN")

input("?")

print("Opening the file...")
target = open(file_name, 'w')

print("Truncating the file. . .")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these lines to file: ")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("Now lets close the file")
target.close()

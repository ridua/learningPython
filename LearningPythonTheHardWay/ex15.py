from sys import argv

script, file_name = argv
txt = open(file_name)
print(txt.read())
#print(txt.readline())


print("Type of filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()

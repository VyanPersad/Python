'Reading from file'
file = open("Test.txt", 'r')
content = file.read()
print(content)

content = file.readlines()
print(content)
file.close()
'Creating a file'
file = open("Test.txt", 'w')
file.write("This is some new text.")
'Appending to a file'
file = open("Test.txt", 'a')
file.write("\nSome more text")
print(content)

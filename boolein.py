myfile = open('io.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)

content= myfile.read()
print(content)
myfile.seek(0)
print(myfile.readline())
print("\n")
with open('io.txt') as io:
    contentone= io.read()

print(contentone)
with open('io.txt', mode='a') as io:
    io.write("\nDAWM")

with open('io.txt', mode='r') as io:
    print(io.read())
    contenttwo = io.read()
print(contenttwo)
with open("test.txt", mode="w") as f:
    f.write("i created this file")
with open('test.txt') as f:
    print(f.read())

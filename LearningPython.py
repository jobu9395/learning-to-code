filename = 'learning_python.txt'

print("---Reading in the entire file")
with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)

print("\n--- Looping over the lines")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n---Storing the lines as a list")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

with open(filename) as f:
    for line in f:
        line = line.rstrip()
        print(line.replace('python', 'C'))




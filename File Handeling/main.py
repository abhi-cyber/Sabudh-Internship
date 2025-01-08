# Open a file for reading
with open('./message.txt', 'r') as file:
    content = file.read()
    print("Reading from file:")
    print(content)

# Open a file for writing (this will overwrite the file if it exists)
with open('./message.txt', 'w') as file:
    file.write("This is a new line.\n")
    file.write("Writing to the file.\n")

# Open a file for appending (this will add to the file without overwriting)
with open('./message.txt', 'a') as file:
    file.write("Appending a new line.\n")

# Open a file for reading again to see the changes
with open('./message.txt', 'r') as file:
    content = file.read()
    print("\nReading from file after writing and appending:")
    print(content)

# Open a file for reading line by line
with open('./message.txt', 'r') as file:
    print("\nReading line by line:")
    for line in file:
        print(line, end='')

# Open a file for reading and writing
with open('./message.txt', 'r+') as file:
    content = file.read()
    file.write("\nAdding a line in read+write mode.\n")
    print("\nReading from file in read+write mode:")
    print(content)
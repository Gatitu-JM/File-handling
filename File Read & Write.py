# File Read & Write Challenge

# Step 1: Read from the original file
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 2: Modify the content (example: convert to uppercase)
modified_content = content.upper()

# Step 3: Write the modified content to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been modified and saved to 'output.txt'.")

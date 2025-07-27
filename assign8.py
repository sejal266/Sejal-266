input_string = "aaabbbcccdddee"

# Convert to uppercase
input_string = input_string.upper()

# Initialize empty string to track counted characters
counted = ""

# Loop through each character
for char in input_string:
    if char not in counted:
        count = 0
        for c in input_string:
            if c == char:
                count += 1
        print(f"{char}= {count}")
        counted += char
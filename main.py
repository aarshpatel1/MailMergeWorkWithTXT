# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# Hint3: This method will also help you: https://www.w3schools.com/python/  ref_string_replace.asp

# for each name in invited_names.txt
name_list = []
with open("Input/Names/invited_names.txt") as invited_names:
    for name in invited_names.readlines(50):
        name_list.append(name.strip())
# print(name_list)

# Replace the [name] placeholder with the actual name.
with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_template = starting_letter.read()
    # Save the letters in the folder "ReadyToSend".
    for letter_to_name in name_list:
        with open(f"Output/ReadyToSend/letter_for_{letter_to_name}", mode="w") as letter_for:
            letter_to = letter_template.replace("[name]", letter_to_name)
            letter_for.write(letter_to)

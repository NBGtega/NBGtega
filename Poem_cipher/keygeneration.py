"""First attempt in creating an encryption algorithm using Poems and Columnar Transposition matrix. More fixes will be worked on"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
done = False
while not done:
    #Collecting user input 
    user_input_one = input("Enter the poem here: ")

    #Master key. This code block will be improved with time. One option is to hide the master key in the encyption cipher produced in the output
    #or choose the master key at random using a random code generator

    user_input_two = input("Enter key here: ")
    if user_input_one == 'quit' or user_input_two == 'quit':
        done = True
    else:

        string_to_list = user_input_one.split()
        collected_words = []
        for character in user_input_two:
            finding_index_of_key = alphabet.find(character)
            if finding_index_of_key == -1:
                print(f"character '{character}' is not in the alphabet")
                continue
            try:
                finding_indexed_words = string_to_list[finding_index_of_key]
                collected_words.append(finding_indexed_words)
                print(f"Word corresponding to '{character}': {finding_indexed_words}")
            except IndexError:
                print(f"No word found in the poem for index {finding_index_of_key}")

        keyword = ''.join(collected_words)
        print(f"Generated Keyword: {keyword}")

        # Generating columnar order based on the keyword
        final_sequence = sorted(range(len(keyword)), key=lambda i: keyword[i])

        plain_text = input("Insert plain text here: ")
        joined_plain_text = ''
        for char in plain_text:
            if char.isalpha():
                joined_plain_text += char.upper()
        print(joined_plain_text)
        num_cols = len(keyword)
        print(num_cols)
        print(len(joined_plain_text))
        num_rows = -(-len(joined_plain_text) // num_cols)
        print(num_rows)

        # Create encryption matrix
        encryption_matrix = []
        text_position_in_matrix = 0
        for row in range(num_rows):
            current_row = []
            for col in range(num_cols):
                if text_position_in_matrix < len(joined_plain_text):
                    current_row.append(joined_plain_text[text_position_in_matrix])
                else:
                    current_row.append('')
                text_position_in_matrix += 1
            encryption_matrix.append(current_row)

        # Print matrix
        for row in encryption_matrix:
            print(' '.join(char if char != '' else 'X' for char in row))

        # First encryption step (keep as is)
        cipher_text_first_step = []
        for col_index_one in final_sequence:
            column_one = []
            for row in encryption_matrix:
                if col_index_one < len(row):  # Remove the '' check since we want X's
                    column_one.append(row[col_index_one])
            cipher_text_first_step.append(''.join(column_one))

        first_encryption = ''.join(cipher_text_first_step)
        print('First encryption:', first_encryption)

        # Generate new sequence based on the first encrypted text
        second_sequence = sorted(range(len(first_encryption[:num_cols])), 
                               key=lambda i: first_encryption[i])




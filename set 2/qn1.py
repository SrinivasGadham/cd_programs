def tokenize(input_text):
    character_count = len(input_text)
    line_count = input_text.count('\n')
    space_count = input_text.count(' ')
    tab_count = input_text.count('\t')

    return character_count, line_count, space_count, tab_count

# Example usage
text = '''
This is a sample text.
It has multiple lines.
There are spaces and	 tabs as well.
'''

char_count, line_count, space_count, tab_count = tokenize(text)

print("Number of characters:", char_count)
print("Number of lines:", line_count)
print("Number of spaces:", space_count)
print("Number of tabs:", tab_count)

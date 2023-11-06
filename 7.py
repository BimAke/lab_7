
#1
import re
def match_string(string):
    pattern = r'a[b]*' 
    match = re.search(pattern, string)
    if match:
        return True
    else:
        return False
#2
import re
def match_string(string):
    pattern = r'a[b]{2,3}' 
    match = re.search(pattern, string)
    if match:
        return True
    else:
        return False
#3
import re
def find_sequences(string):
    pattern = r'[a-z]+_[a-z]+' 
    sequences = re.findall(pattern, string)
    return sequences
#4
import re
def find_sequences(string):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, string)
    return sequence
#5
import re
def match_string(string):
    pattern = r'a.*b$'
    match = re.match(pattern, string)
    if match:
        print("String matches the pattern")
    else:
        print("String does not match the pattern")
#6
def replace_characters(string):
    pattern = r'[ ,.]'
    replaced_string = re.sub(pattern, ':', string)
    return replaced_string
#7
def snake_to_camel(snake_case_string):
    words = snake_case_string.split('_')
    camel_case_string = words[0].lower() + ''.join(word.title() for word in words[1:])
    return camel_case_string
#8
def split_at_uppercase(string):
    result = []
    current_word = ''
    for char in string:
        if char.isupper():
            if current_word:
                result.append(current_word)
            current_word = char
        else:
            current_word += char
    if current_word:
        result.append(current_word)
#9
def insert_spaces(string):
    result = ''
    for i in range(len(string)):
        if i > 0 and string[i].isupper() and string[i-1].islower():
            result += ' '
        result += string[i]
#10
def camel_to_snake(string):
    result = ''
    for i in range(len(string)):
        if string[i].isupper() and i > 0:
            result += '_'
        result += string[i].lower()
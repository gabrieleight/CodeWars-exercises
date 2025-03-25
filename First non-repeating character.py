"""
Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");
"""

def first_non_repeating_letter(string):
    string_normal = string.lower()
    for i in string_normal:
        ocorrencias = string_normal.count(i)
        if ocorrencias == 1:
            return string[string_normal.find(i)]
    if ocorrencias > 1 or string_normal == "":
        return ""
            
if __name__ == "__main__":
    string = "hello world, eh?"
    print(first_non_repeating_letter(string))
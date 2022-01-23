import string
from string import digits

def is_pangram(sentance):
    lower_case = sentance.lower()
    no_space = lower_case.replace(" ", "")
    table = str.maketrans("", "", digits)
    no_digits = no_space.translate(table)
    table = str.maketrans(dict.fromkeys(string.punctuation))
    no_punc = no_digits.translate(table)  
    unique_letters = len(set(no_punc))
    if unique_letters == 26:
        return True
    else:
        return False
    
    
    
    
print(is_pangram("hello my name is laura and I am 35"))
print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
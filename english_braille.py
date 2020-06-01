# Part 5
# Author: Tahseen Bin Taj

from text_to_braille import *
from char_to_braille import *
from helpers import *

ENG_CAPITAL = '..\n..\n.o'
OPEN_QUOTE = '“'
OPEN_QUOTE_OSTRING = '..\no.\noo'
CLOSE_QUOTE_OSTRING = '..\n.o\noo'
CLOSE_QUOTE = '”'
ALL_CAPS = '.o\n..\n.o\n\n'*2
ENG_ALL_CAPS = (ENG_CAPITAL + '\n\n')*2
END_NUM = '..\n.o\n.o'
ENG_QUESTION = OPEN_QUOTE_OSTRING
# You may want to define more global variables here

####################################################
# Here are two helper functions to help you get started

def two_letter_contractions(text):
    '''(str) -> str
    Process English text so that the two-letter contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.
    Provided to students. You should not edit it.

    >>> two_letter_contractions('chat')
    'âat'
    >>> two_letter_contractions('shed')
    'îë'
    >>> two_letter_contractions('shied')
    'îië'
    >>> two_letter_contractions('showed the neighbourhood where')
    'îœë ôe neiêbürhood ûïe'
    >>> two_letter_contractions('SHED')
    'ÎË'
    >>> two_letter_contractions('ShOwEd tHE NEIGHBOURHOOD Where') 
    'ÎŒË tHE NEIÊBÜRHOOD Ûïe'
    '''
    combos = ['ch', 'gh', 'sh', 'th', 'wh', 'ed', 'er', 'ou', 'ow']
    for i, c in enumerate(combos):
        text = text.replace(c, LETTERS[-1][i])
    for i, c in enumerate(combos):
        text = text.replace(c.upper(), LETTERS[-1][i].upper())
    for i, c in enumerate(combos):
        text = text.replace(c.capitalize(), LETTERS[-1][i].upper())

    return text


def whole_word_contractions(text):
    '''(str) -> str
    Process English text so that the full-word contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    If the full-word contraction appears within a word, 
    contract it. (e.g. 'and' in 'sand')

    Provided to students. You should not edit this function.

    >>> whole_word_contractions('with')
    'ù'
    >>> whole_word_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meow'
    >>> whole_word_contractions('With')
    'Ù'
    >>> whole_word_contractions('WITH')
    'Ù'
    >>> whole_word_contractions('wiTH')
    'wiTH'
    >>> whole_word_contractions('FOR thE Cat WITh THE purr And The meow')
    'É thE Cat WITh À purr Ç À meow'
    >>> whole_word_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> whole_word_contractions('wither')
    'ùer'
    '''
    # putting 'with' first so wither becomes with-er not wi-the-r
    words = ['with', 'and', 'for', 'the']
    fr_equivs = ['ù', 'ç', 'é', 'à', ]
    # lower case
    for i, w in enumerate(words):
        text = text.replace(w, fr_equivs[i])
    for i, w in enumerate(words):
        text = text.replace(w.upper(), fr_equivs[i].upper())
    for i, w in enumerate(words):
        text = text.replace(w.capitalize(), fr_equivs[i].upper())
    return text



####################################################
# These two incomplete helper functions are to help you get started

def convert_contractions(text):
    '''(str) -> str
    Convert English text so that both whole-word contractions
    and two-letter contractions are changed to the appropriate
    French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    Refer to the docstrings for whole_word_contractions and 
    two_letter_contractions for more info.

    >>> convert_contractions('with')
    'ù'
    >>> convert_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meœ'
    >>> convert_contractions('chat')
    'âat'
    >>> convert_contractions('wither')
    'ùï'
    >>> convert_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> convert_contractions('Showed The Neighbourhood Where')
    'Îœë À Neiêbürhood Ûïe'
    '''
    # ADD CODE HERE
    return two_letter_contractions(whole_word_contractions(text))


def convert_quotes(text):
    '''(str) -> str
    Convert the straight quotation mark into open/close quotations.
    >>> convert_quotes('"Hello"')
    '“Hello”'
    >>> convert_quotes('"Hi" and "Hello"')
    '“Hi” and “Hello”'
    >>> convert_quotes('"')
    '“'
    >>> convert_quotes('"""')
    '“”“'
    >>> convert_quotes('" "o" "i" "')
    '“ ”o“ ”i“ ”'
    '''
    # ADD CODE HERE
    count = 0
    for i,c in enumerate(text):
        if c == '"':
            count += 1
            if count % 2 == 1:
                # replace only the first occurrence
                text = text.replace(text[i], OPEN_QUOTE, 1)
            else:
                text = text.replace(text[i], CLOSE_QUOTE, 1)
    return text 


####################################################
# Put your own helper functions here!
def convert_parentheses(text):
    '''(str) -> str
    Convert open/close parentheses to the appropriate English braille unicode versions.
    >>> convert_parentheses('(⠓⠊)')
    '⠶⠓⠊⠶'
    >>> convert_parentheses('(⠠)⠯ ⠠⠯( ⠁⠠⠝)')
    '⠶⠠⠶⠯ ⠠⠯⠶ ⠁⠠⠝⠶'
    >>> convert_parentheses('()((⠕⠍')
    '⠶⠶⠶⠶⠕⠍'
    '''
    text = text.replace('(', ostring_to_unicode('..\noo\noo'))
    text = text.replace(')', ostring_to_unicode('..\noo\noo'))
    return text


def convert_numbers(text):
    '''(str) -> str
    Convert French braille numbering system to English braille numbering system.
    >>> convert_numbers('⠼⠃⠼⠚⠁⠼⠃') # '20a2'
    '⠼⠃⠚⠰⠁⠼⠃⠰'
    >>> convert_numbers('⠨⠨⠉⠕⠍⠏ ⠼⠃⠼⠚⠼⠃') # 'COMP 202'
    '⠨⠨⠉⠕⠍⠏ ⠼⠃⠚⠃⠰'
    >>> convert_numbers('⠨⠨⠉⠕⠍⠏ ⠼⠃⠼⠚⠼⠃ ⠨⠨⠁⠝⠙ ⠨⠨⠉⠕⠍⠏ ⠼⠃⠼⠑⠼⠚') # 'COMP 202 AND COMP 250'
    '⠨⠨⠉⠕⠍⠏ ⠼⠃⠚⠃⠰ ⠨⠨⠁⠝⠙ ⠨⠨⠉⠕⠍⠏ ⠼⠃⠑⠚⠰'
    '''
    unicode_num = ostring_to_unicode(NUMBER)
    count = 0
    res = ''
    for i,c in enumerate(text):
        # This if statement checks if it is the first occurrence (first number) in the string and initializes
        # it. And the counter increments by 1.
        if c == unicode_num and count == 0:
            count += 1
            res += unicode_num
        # This if statement checks if it is a continuous sequence of numbers and skips further initialization.
        # And the counter increments by 1.
        elif c == unicode_num and count >0:
            count += 1
        # This if statement checks whether the current character is a number and the next character is
        # not a number, if the next character is within range, otherwise it checks whether it is the
        # last character of a string so that the number sequence can be indicated to end. The counter is therefore set to 0.
        elif text[i-1] == unicode_num and (i+1 < len(text) and text[i+1] != unicode_num) or (text[i-1] == unicode_num and i+1 == len(text)):
            count = 0
            res += c + ostring_to_unicode('..\n.o\n.o')
        # Any other character is added to the result string as is.
        else:
            res += c
    return res


####################################################

def english_text_to_braille(text):
    '''(str) -> str
    Convert text to English Braille. Text could contain new lines.

    This is a big problem, so think through how you will break it up
    into smaller parts and helper functions.
    Hints:
        - you'll want to call text_to_braille
        - you can alter the text that goes into text_to_braille
        - you can alter the text that comes out of text_to_braille
        - you shouldn't have to manually enter the Braille for 'and', 'ch', etc

    You are expected to write helper functions for this, and provide
    docstrings for them with comprehensive tests.

    >>> english_text_to_braille('202') # numbers
    '⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('2') # single digit
    '⠼⠃⠰'
    >>> english_text_to_braille('COMP') # all caps
    '⠠⠠⠉⠕⠍⠏'
    >>> english_text_to_braille('COMP 202') # combining number + all caps
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('and')
    '⠯'
    >>> english_text_to_braille('and And AND aNd')
    '⠯ ⠠⠯ ⠠⠯ ⠁⠠⠝⠙'
    >>> english_text_to_braille('chat that the with')
    '⠡⠁⠞ ⠹⠁⠞ ⠷ ⠾'
    >>> english_text_to_braille('hi?')
    '⠓⠊⠦'
    >>> english_text_to_braille('(hi)')
    '⠶⠓⠊⠶'
    >>> english_text_to_braille('"hi"')
    '⠦⠓⠊⠴'
    >>> english_text_to_braille('COMP 202 AND COMP 250')
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰ ⠠⠯ ⠠⠠⠉⠕⠍⠏ ⠼⠃⠑⠚⠰'
    >>> english_text_to_braille('For shapes with colour?')
    '⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠦'
    >>> english_text_to_braille('(Parenthetical)\\n\\n"Quotation"')
    '⠶⠠⠏⠁⠗⠑⠝⠷⠞⠊⠉⠁⠇⠶\\n\\n⠦⠠⠟⠥⠕⠞⠁⠞⠊⠕⠝⠴'
    '''
    # Here's a line we're giving you to get started: change text so the
    # contractions become the French accented letter that they correspond to
    text = convert_contractions(text)

    # Run the text through the converter which converts regular quotes into more specific quotes
    text = convert_quotes(text)

    # Run the text through the French Braille translator
    text = text_to_braille(text)
    
    # Set the braille formats of '(' and ')' as themselves temporarily so that
    # they do not mix up with quotation marks and can be operated on individually.
    text = text.replace(ostring_to_unicode('..\no.\noo'), '(')
    text = text.replace(ostring_to_unicode('..\n.o\noo'), ')')
    
    # Replace the French capital with the English capital
    text = text.replace(ostring_to_unicode(CAPITAL), ostring_to_unicode(ENG_CAPITAL))
    
    # Replace the French all caps with the English all caps
    text = text.replace(ostring_to_unicode(ALL_CAPS), ostring_to_unicode(ENG_ALL_CAPS))

    # Convert the French formatted quotations and questions to the corresponding English versions
    text = text.replace(OPEN_QUOTE,ostring_to_unicode(OPEN_QUOTE_OSTRING))
    text = text.replace(CLOSE_QUOTE,ostring_to_unicode(CLOSE_QUOTE_OSTRING))
    text = text.replace(ostring_to_unicode(char_to_braille('?')),ostring_to_unicode(ENG_QUESTION))

    # Convert the French styled parentheses to the English styled parentheses
    text = convert_parentheses(text)
    
    # Convert the French numbering system to the English numbering system
    text = convert_numbers(text)
    
    return text


def english_file_to_braille(fname):
    '''(str) -> NoneType
    Given English text in a file with name fname in folder tests/,
    convert it into English Braille in Unicode.
    Save the result to fname + "_eng_braille".
    Provided to students. You shouldn't edit this function.

    >>> english_file_to_braille('test4.txt')
    >>> file_diff('tests/test4_eng_braille.txt', 'tests/expected4.txt')
    True
    >>> english_file_to_braille('test5.txt')
    >>> file_diff('tests/test5_eng_braille.txt', 'tests/expected5.txt')
    True
    >>> english_file_to_braille('test6.txt')
    >>> file_diff('tests/test6_eng_braille.txt', 'tests/expected6.txt')
    True
    '''  
    file_to_braille(fname, english_text_to_braille, "eng_braille")


if __name__ == '__main__':
    doctest.testmod()    # you may want to comment/uncomment along the way
    # and add tests down here

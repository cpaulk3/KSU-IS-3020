
def words_string_ag():
    quote = input("enter a 1 sentence quote, non-alpha separate words:")
    word = ''
        
    for character in quote:
        if character.isalpha() == True:
            word += character 
        else:
            if word.lower() >= 'h':
                print(word.upper())
                word = ''
    if word.lower() >= 'h':
        print(word.upper())
words_string_ag()

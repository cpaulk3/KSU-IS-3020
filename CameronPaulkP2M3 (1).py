index = 0
user_input = input("Enter a saying or poem: ")
words_list = user_input.split()
words_new_list = []
new_list = [] 
 
while index < len(words_list):
    if len(words_list[index]) < 4:
        words_new_list.append(words_list[index].lower())
        index += 1
    elif len(words_list[index]) > 6:
        words_new_list.append(words_list[index].upper())
        index += 1
    else:
        words_new_list.append(words_list[index])
        index += 1
         
def word_mixer(words_new_list):
    words_new_list.sort()
    while len(words_new_list) > 5:
        new_list.append(words_new_list.pop(-5))
        new_list.append(words_new_list.pop(0))
        new_list.append(words_new_list.pop()+"\n")
        joined = " ".join(new_list)
         
    print(joined)
 
test = word_mixer(words_new_list)

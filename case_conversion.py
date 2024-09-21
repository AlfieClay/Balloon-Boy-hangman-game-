lower_case='abcdefghijklmnopqrstuvwxyz'
upper_case='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def upper_to_lower(upper_word): #convert an upper case to a lower case word
    first_upper=upper_word[0]
    for i in range(int(len(upper_case)-1)):
                   char=upper_case[i]
                   if char==first_upper:
                       upper_index=i
                   else:
                        pass
    first_lower=lower_case[upper_index]
    lower_word=first_lower+upper_word[1:]
    return lower_word
def lower_to_upper(lower_word): #convert a lower case to an upper case upper
    lower_word=str(lower_word)
    first_lower=lower_word[0]
    for i in range(int(len(lower_case)-1)):
                   char=lower_case[i]
                   if char==first_lower:
                        lower_index=i
                        lower_index=int(lower_index)
                        break
                   else:
                        pass
    first_upper=upper_case[lower_index]
    upper_word=first_upper+lower_word[1:]
    return upper_word
def upper_to_lower_list(list_1): #convert a list of upper case words to lower case (starting) words
    list_2=[]
    for upper_word in list_1:
        lower_word=upper_to_lower(upper_word)
        list_2.append(lower_word)
    return list_2
def lower_to_upper_list(list_1): #convert a list of upper case words to lower case (starting) words
    list_2=[]
    for lower_word in list_1:
        upper_word=lower_to_upper(lower_word)
        list_2.append(upper_word)
    return list_2



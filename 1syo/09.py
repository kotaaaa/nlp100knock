import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."



words = [word.strip(".,") for word in s.split()]
print (words)





def typoglycemia(target):


    result = []
    for t in target.split():
        # print (word)
        if len(t) <= 3:
            result.append(t)
        else:
            char_list = list(t[1:-1])
            random.shuffle(char_list)
            result.append(t[0] + ''.join(char_list) + t[-1])
    return result
    # return ''.join(result)

s = typoglycemia(s)

print(s)







##

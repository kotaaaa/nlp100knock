

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."


r = s.split()


count = 0
for i in r:
    for char in i:
        count += 1
        # print (count)
        # print (i)
    print (i)
    print ("文字数=", count)
    count = 0


# for i in r:
#     if i=1,5,6,7,8,9,15,16
#         s =
#
# a =




word_index = {};
for i, word in enumerate(r):
    n = i + 1;
    if n in [1,5,6,7,8,9,15,16,19]:
        word_index[word[:1]] = n;
    else:
        word_index[word[:2]] = n;
    print (word_index);

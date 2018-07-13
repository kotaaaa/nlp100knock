# s = "stressed"
#
# print (s[::-1])
#
#
# w = "パトカタクシー"
#
# print (w[::2])
#
# a = "watashida"
#
# print (a[::-1])



s1 = "パトカー"
s2 = "タクシー"
s3 = ""

for moji1, moji2 in zip(s1,s2):
    s3 = s3 + moji1 + moji2
    print (s3);


s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"

# print(s)


r = s.split()


print(r)

# count = 0
# for i in r:
#     for char in r[i]:
#         count += 1
#         print (count)
#         print (r[i])


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
#     print (i)











##

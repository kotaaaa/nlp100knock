
s = "paraparaparadise"
t = "paragraph"


chargrams = [s[i:i+2] for i in range(len(s))]
chargramt = [t[i:i+2] for i in range(len(t))]



print(chargrams)
print(chargramt)

# for i in chargrams:
#     wa = chargrams if (chargrams[i] == chargramt[i]):

# print(wa)
##
# print (chargrams&chargramt)
# print (str(chargrams-chargramt))


X = set(chargrams)
Y = set(chargramt)



print (str(X|Y))
print (str(X&Y))













##

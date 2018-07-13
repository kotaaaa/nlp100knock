s = "Happy Birthday to you, Mr coffee"

print(s)



i = 1
chargram = [s[i:i+5] for i in range(len(s))]

print(chargram)


words = [word.strip(".,") for word in s.split()]
print (words)





words = [word for word in s.split()]
print(words)
##

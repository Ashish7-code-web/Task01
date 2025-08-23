def anagram(l1,l2):
    if sorted(l1)==sorted(l2):
        print("Anagram")
    else:
        print("Not a Anagram")    
a = "listen"
b = "silent"
anagram(a,b)
def caesarCipher(s, k):
    # Write your code here 
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            new_s = ord(s[i]) + k 
            #소문자 97~122
            if s[i].islower() and new_s > 122:
                new_s = 97+ (new_s % 123)
            
            #대문자 65~90     
            elif s[i].islower() and new_s > 90:
                new_s = 91 + (new_s % 91)
                
            s[i] = chr(new_s)
    print ("".join(s))

n = 11
s = "middle-Outz"
k = 2

caesarCipher(s,k)

#So this is weird, I'm going to add the link below but for some reason the tutorial had there script print out the entire ciphered
#string but mine will only print out the first character in the string for some reason, looking into it more tomorrow...
#https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm

#I've changed a bit to get some input stuff and such but again, baby steps

def encrypt(text,s):
   result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
      return result
#check above function 
text = input("what would you like to encrypt?: ")
s = input("how many rotations would you like? (1-26): ")

print("Plain text: " + text)
print("Shift pattern: " + str(s))
print("Cipher: " + encrypt(text, int(s)))

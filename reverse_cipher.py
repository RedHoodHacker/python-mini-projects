

#https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_reverse_cipher.htm

message = input("What would you like to encrypt? : ")

translated = ' ' 

i  = len(message) - 1 

while i >= 0:
	translated = translated + message[i]
	i = i -1 
print("ciphered: " + translated)

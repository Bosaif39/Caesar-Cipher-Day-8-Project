def caesar (shift,text,direction):
    
    """
    Encode or decode the given text using the Caesar cipher.
    
    shift (int): The number of positions each letter in the text should be shifted.
    text (str): The text to be encoded or decoded.
    direction (str): The operation to perform; "encode" for encoding,"decode" for decoding.

    Example:
        caesar(3, "hello", "encode") -> "khoor"
        caesar(3, "khoor", "decode") -> "hello"
        
    How it works: 

        1-Get each character in the text by using for loop
        2-Check if it's in the alphabet and get the index
        3-Shiting the index to encode or decode 
        4-add the new letter to the text 
        5-if it's not in the alphabet just add it as its 
        
    """
    
    cipherText=""
    for i in text:
        if i in alphabet:
            pos=alphabet.index(i)
            if(direction=="encode"):
                pos=pos+shift
            elif(direction=="decode"):
                pos=pos-shift
            cipherText=cipherText+alphabet[pos]
        else:
            cipherText=cipherText+i

    print(f"The {direction}d text is {cipherText}")


alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


looper=True

"""
This loop get the input from the user and keeps repating until the user type no.

"""
while looper:
    direction=input("Type 'encode' to encrypt or type 'decode' to decrypt:\n")
    text =input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    shift=shift % 26
    caesar (shift=shift,text=text,direction=direction)
    ans =input("Type 'no' if you are done. Otherwise type anything else to continue:\n").lower()
    print("==="*10)
    if(ans=="no"):
        break

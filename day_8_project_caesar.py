#A function to encode or decode the text using the Caesar cipher. It shifts the letters in the text by the specified amount.
def caesar (shift,text,direction):
    caesar=""
    for i in text:
        if i in alphabrt:
            pos=alphabrt.index(i)
            if(direction=="encode"):
                pos=pos+shift
            elif(direction=="decode"):
                pos=pos-shift
            cipher=cipher+alphabrt[pos]
        else:
            cipher=cipher+i

    print(f"The {direction}d text is {cipher}")

#A list for letters
alphabrt=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#A key to break the loop
ans="yes"

#While loop to use the function
while(ans=="yes"):
    direction=input("Type encode to encryptm type decode to decrypt:\n")
    text =input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    shift=shift % 26
    caesar (shift=shift,text=text,direction=direction)
    ans =input("Type yes if you want to go again. Otherwise type no:\n").lower()


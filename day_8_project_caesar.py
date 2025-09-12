def caesar_cipher(shift_amount, message, mode):
    """
    Encode or decode the given message using the Caesar cipher.
    
    shift_amount (int): The number of positions each letter in the message should be shifted.
    message (str): The text to be encoded or decoded.
    mode (str): The operation to perform; "encode" for encoding, "decode" for decoding.

    Example:
        caesar_cipher(3, "hello", "encode") -> "khoor"
        caesar_cipher(3, "khoor", "decode") -> "hello"
        
    How it works: 
        1 - Iterate through each character in the message
        2 - If it's in the alphabet, get its index
        3 - Shift the index depending on encode/decode
        4 - Append the new letter to the result
        5 - If it's not in the alphabet, add it unchanged
    """
    
    result_text = ""
    for char in message:
        if char in alphabet:
            char_index = alphabet.index(char)
            if mode == "encode":
                char_index += shift_amount
            elif mode == "decode":
                char_index -= shift_amount
            result_text += alphabet[char_index]
        else:
            result_text += char

    print(f"The {mode}d text is {result_text}")


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


continue_running = True

"""
This loop keeps asking for user input until they type 'no'.
"""
while continue_running:
    mode = input("Type 'encode' to encrypt or type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))
    shift_amount = shift_amount % 26
    caesar_cipher(shift_amount, message, mode)

    user_choice = input("Type 'no' if you are done. Otherwise type anything else to continue:\n").lower()
    print("===" * 10)
    if user_choice == "no":
        continue_running = False

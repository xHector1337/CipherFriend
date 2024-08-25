import cipher

def decode(text):
    print("Rot13:",cipher.rot13decode(text))
    try:
        print("Base64:",cipher.b64(text))
    except:
        print("Base64: None")
    try:
        print("Base32:",cipher.b32(text))
    except:
        print("Base32: None")    
    try:
        print("Base16:",cipher.b16(text))
    except:
        print("Base16: None")
    try:        
        print("Base85:",cipher.b85(text))
    except:
        print("Base85: None")
    try:        
        print("Ascii85:",cipher.a85(text))
    except:
        print("Ascii85: None")
    print("Morse:",cipher.MorseCodeDecode(text))
    print("Url Decode:",cipher.urlDecode(text))
    print("Reverse:",cipher.reverse(text))        

def encode(text):
    print("Rot13:",cipher.rot13(text))
    print("Base64:",cipher.b64encode(text))
    print("Base32:",cipher.b32encode(text))
    print("Base16:",cipher.b16encode(text))
    print("Base85:",cipher.b85encode(text))
    print("Ascii85:",cipher.a85encode(text))
    print("Morse:",cipher.MorseCodeEncode(text))
    print("Url Encode:",cipher.urlEncode(text))
    print("Reverse:",cipher.reverse(text))

def main():
    mode = str(input("Enter cipher mode: (encode or decode)\n"))
    while mode != "encode" and mode != "decode":
        mode = str(input("Enter cipher mode: (encode or decode)\n"))
    if mode == "encode":
        text = str(input("Enter your text to be encoded:\n"))
        encode(text)
    elif mode == "decode":
        text = str(input("Enter your text to be decoded:\n"))
        decode(text)
main()                   

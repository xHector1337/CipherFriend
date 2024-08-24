import codecs
import base64
def rot13(text):
    return codecs.encode(text,"rot13")
def b64(text):
    if len(text.split(" ")) > 1:
        return "None" 
    return base64.b64decode(text).decode('utf-8')
def b32(text):
    if len(text.split(" ")) > 1:
        return "None"
    return base64.b32decode(text).decode('utf-8')
def b16(text):
    if len(text.split(" ")) > 1:
        return "None"
    return base64.b32decode(text).decode('utf-8')
def b85(text):
    if len(text.split(" ")) > 1:
        return "None"
    return base64.b85decode(text).decode('utf-8')
def hex(text):
    count = 0
    hexString = ""
    string =  text.encode().hex()
    for i in string:
        count += 1
        hexString += i
        if count % 2 == 0:
            hexString += " "
    return hexString     
def a85(text):
    if len(text.split(" ")) > 1:
        return "None"
    return base64.a85decode(text).decode('utf-8')
def b64encode(text):
    return base64.b64encode(text).decode('utf-8')
def b32encode(text):
    return base64.b32encode(text).decode('utf-8')
def b16encode(text):
    return base64.b16encode(text).decode('utf-8')
def b85encode(text):
    return base64.b85encode(text).decode('utf-8')
def a85encode(text):
    return base64.a85encode(text).decode('utf-8')

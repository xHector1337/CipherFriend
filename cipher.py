import codecs
import base64
import hashlib
import urllib.parse
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
    return base64.b64encode(text.encode()).decode('utf-8')
def b32encode(text):
    return base64.b32encode(text.encode()).decode('utf-8')
def b16encode(text):
    return base64.b16encode(text.encode()).decode('utf-8')
def b85encode(text):
    return base64.b85encode(text.encode()).decode('utf-8')
def a85encode(text):
    return base64.a85encode(text.encode()).decode('utf-8')
def rot13decode(text):
    return codecs.decode(text,"rot13")
def MorseCodeEncode(text):
    A = ".-"
    B = "-..." 
    C = "-.-."
    D = "-.."
    E = "."
    F = "..-."
    G = "--."
    H = "...."
    I = ".."
    J = ".---"
    K = "-.-"
    L = ".-.."
    M = "--"
    N = "-."
    O = "---"
    P = ".--."
    Q = "--.-"
    R = ".-."
    S = "..."
    T = "-"
    U = "..-"
    V = "...-"
    W = ".--"
    X = "-..-"
    Y = "-.--"
    Z = "--.."
    Ö = "---."
    Ü = "..--"
    Zero = "-----"
    One  = ".----"
    Two = "..---"
    Three = "...--"
    Four = "....-"
    Five = "....."
    Six = "-...."
    Seven = "--..."
    Eight = "---.."
    Nine = "----."
    Dot = ".-.-.-"
    Comma = "--..--"
    QuestionMark = "..--.."
    ExclamationMark = "-.-.--"
    Colon = "---..."
    QuotationMark = ".-..-."
    SingleQuotation = ".----."
    Equal = "-...-"
    return text.upper().replace(".",f"{Dot} ").replace("A",f"{A} ").replace("B",f"{B} ").replace("C",f"{C} ").replace("D",f"{D} ").replace("E",f"{E} ").replace("F",f"{F} ").replace("G",f"{G} ").replace("H",f"{H} ").replace("I",f"{I} ").replace("J",f"{J} ").replace("K",f"{K} ").replace("L",f"{L} ").replace("M",f"{M} ").replace("N",f"{N} ").replace("O",f"{O} ").replace("P",f"{P} ").replace("Q",f"{Q} ").replace("R",f"{R} ").replace("S",f"{S} ").replace("T",f"{T} ").replace("U",f"{U} ").replace("V",f"{V} ").replace("W",f"{W} ").replace("X",f"{X} ").replace("Y",f"{Y} ").replace("Z",f"{Z} ").replace("Ö",f"{Ö} ").replace("Ü",f"{Ü} ").replace("0",f"{Zero} ").replace("1",f"{One} ").replace("2",f"{Two} ").replace("3",f"{Three} ").replace("4",f"{Four} ").replace("5",f"{Five} ").replace("6",f"{Six} ").replace("7",f"{Seven} ").replace("8",f"{Eight} ").replace("9",f"{Nine} ").replace(",",f"{Comma} ").replace("?",f"{QuestionMark} ").replace("!",f"{ExclamationMark} ").replace(":",f"{Colon} ").replace('"',f"{QuotationMark} ").replace("'",f"{SingleQuotation} ").replace("=",f"{Equal} ")

def MorseCodeDecode(text):
    A = ".-"
    B = "-..." 
    C = "-.-."
    D = "-.."
    E = "."
    F = "..-."
    G = "--."
    H = "...."
    I = ".."
    J = ".---"
    K = "-.-"
    L = ".-.."
    M = "--"
    N = "-."
    O = "---"
    P = ".--."
    Q = "--.-"
    R = ".-."
    S = "..."
    T = "-"
    U = "..-"
    V = "...-"
    W = ".--"
    X = "-..-"
    Y = "-.--"
    Z = "--.."
    Ö = "---."
    Ü = "..--"
    Zero = "-----"
    One  = ".----"
    Two = "..---"
    Three = "...--"
    Four = "....-"
    Five = "....."
    Six = "-...."
    Seven = "--..."
    Eight = "---.."
    Nine = "----."
    Dot = ".-.-.-"
    Comma = "--..--"
    QuestionMark = "..--.."
    ExclamationMark = "-.-.--"
    Colon = "---..."
    QuotationMark = ".-..-."
    SingleQuotation = ".----."
    Equal = "-...-"
    translatedText = ""
    text = text.strip("/")
    for i in text.split(" "):
        if i == A:
            translatedText += "a"
        elif i == B:
            translatedText += "b"
        elif i == C:
            translatedText += "c"
        elif i == D:
            translatedText += "d"
        elif i == E: 
            translatedText += "e"
        elif i == F:
            translatedText += "f"
        elif i == G:
            translatedText += "g"
        elif i == H:
            translatedText += "h"
        elif i == I:
            translatedText += "i"
        elif i == J:
            translatedText += "j"
        elif i == K:
            translatedText += "k"
        elif i == L:
            translatedText += "l"
        elif i == M:
            translatedText += "m"
        elif i == N:
            translatedText += "n"
        elif i == O:
            translatedText += "o"
        elif i == P:
            translatedText += "p"
        elif i == Q:
            translatedText += "q"
        elif i == R:
            translatedText += "r"
        elif i == S:
            translatedText += "s"
        elif i == T:
            translatedText += "t"
        elif i == U:
            translatedText += "u"
        elif i == V:
            translatedText += "v"
        elif i == W:
            translatedText += "w"
        elif i == X:
            translatedText += "x"
        elif i == Y:
            translatedText += "y"
        elif i == Z:
            translatedText += "z"
        elif i == Zero:
            translatedText += "0"
        elif i == One:
            translatedText += "1"
        elif i == Two:
            translatedText += "2"
        elif i == Three:
            translatedText += "3"
        elif i == Four:
            translatedText += "4"
        elif i == Five:
            translatedText += "5"
        elif i == Six:
            translatedText += "6"
        elif i == Seven:
            translatedText += "7"
        elif i == Eight:
            translatedText += "8"
        elif i == Nine:
            translatedText += "9"
        elif i == Dot:
            translatedText += "."
        elif i == Comma:
            translatedText += ","
        elif i == Colon:
            translatedText += ":"
        elif i == QuestionMark:
            translatedText += "?"
        elif i == ExclamationMark:
            translatedText += "!"
        elif i == QuotationMark:
            translatedText += '"'
        elif i == SingleQuotation:
            translatedText += "'"
        elif i == Equal:
            translatedText += "="
    if len(translatedText) < 2:
        return "None"                                                                                                                                                                            
    return translatedText

def md5sum(text):
    h = hashlib.md5(text.encode())
    return h.hexdigest()
def sha256sum(text):
    h = hashlib.sha256(text.encode())
    return h.hexdigest()
def sha1sum(text):
    h = hashlib.sha1(text.encode())
    return h.hexdigest()
def sha224sum(text):
    h = hashlib.sha224(text.encode())
    return h.hexdigest()
def sha512sum(text):
    h = hashlib.sha512(text.encode())
    return h.hexdigest()
def sha384sum(text):
    h = hashlib.sha384(text.encode())
    return h.hexdigest()   

def urlEncode(text):
    return urllib.parse.quote(text,safe="")
def urlDecode(text):
    return urllib.parse.unquote(text)
def reverse(text):
    return text[::-1]
    

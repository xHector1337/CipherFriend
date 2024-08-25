Cipher Friend is an app that encodes/decodes the text you write in various encodings. It is written with built-in Python libraries.

# Usage

## Interactive Mode

After cloning or downloading the repository run it by either typing `python main.py` or executing `main.py` with Python.
Then, enter the mode you want to use. (encode or decode)
Finally, enter the text you want to do the operation and see your results :')

## Terminal Mode

After cloning or downloading the repository run it by typing `python main.py --terminal --mode encode --text Hello ` on command line. 
You can change `encode` mode with `decode` mode and you can write the text you want to do operation after `--text` parameter.
Finally, you can get your results.

# Cipher Friend Library Usage
If you want to use Cipher Friend in your code, you can basically do that by importing `cipher.py`.
```
import cipher
```
It uses built-in Python functions so no need to extra downloading!
All of the functions take text argument in string type. 
Here is full list of the commands:

+ rot13(text) --> It encodes the text in rot13.

+ b64(text) --> It decodes the text in base64

+ b32(text) --> It decodes the text in base32.

+ b16(text) --> It decodes the text in base16.

+ b85(text) --> It decodes the text in base85.

+ hex(text) --> It encodes the text in hex.

+ a85(text) --> It decodes the text in ascii85.

+ b64encode(text) --> It encodes the text in base64.

+ b32encode(text) --> It encodes the text in base32.

+ b16encode(text) --> It encodes the text in base16.

+ b85encode(text) --> It encodes the text in base85.

+ a85encode(text) --> It encodes the text in ascii85.

+ rot13decode(text) --> It decodes the text in rot13.

+ MorseCodeEncode(text) --> It encodes the text in Morse.

+ MorseCodeDecode(text) --> It decodes the text in Morse.

+ md5sum(text) --> It hashes the text in md5.

+ sha256sum(text) --> It hashes the text in sha256.

+ sha1sum(text) --> It hashes the text in sha1.

+ sha224sum(text) --> It hashes the text in sha224.

+ sha512sum(text) --> It hashes the text in sha512.

+ sha384sum(text) --> It hashes the text in sha384.

+ urlEncode(text) --> It encodes the text in url encode.

+ urlDecode(text) --> It decodes the text in url encode.

+ reverse(text) --> It returns the text in reverse order.

Happy coding!                

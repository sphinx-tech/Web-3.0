# Web-3.0


# Assignment 1
Basic Python code (using hashlib crypto library) to find nounce such that given an imput string as block header the SHA256("Header"+"nounce") is less than a prespecified target hash.


As the hex() function in python truncates the zero padding when converting integer into hexadecimal fomat;
we have implemented a custom function  padded_hex() referenced from a stackexchange forum to maintain the consistency in conversion from intger in decimal to hexadecimal format - that takes as arguments 
1. the integer to convert to hexadecimal
2. the legnth of characters to denote the hexadecimal number with (extra MSB are padded with zeros)

Finally, the value of nounce alongwith the total execution time is displayed

# AE3KR-task01-AffineCipher

## task description

The description was done during lessons and you should mainly také knowledge from them.
It the simple mono-alphabetical substitution, where the alphabet is only letters A .. Z, which are 
mapped to the indexes 0 .. 25
The cipher-text could be obtained with formula 
CT = (a*OT + b) mod 26
where: a, b are key and make the shifting..
For the example. CT = (3*OT + 5) mod 26 (Thus letter A will be encrypted as F)
Important note – The number a cant be divided with 26 without remaining. -> GCD of 
values a and 26 must be equal to 1.
Your task is to implement 2 functions. First for encryption of any string and the second to 
decryption.
The values a and b should be possible to set by the user.
Maximal amount of the points from the task is 10 points and i tis according to the following parts.
• 2 points for filtration of the open-text (all interpunction should be removed as the special 
characters, etc.). So everything will be changed to only letters A .. Z. The spaces should 
remain and before encryption should be substitued by string „XSPACEX“ -> and accordingly 
the „XSPACEX“ should be changed back to space after decryption. For the example.
OT = „Hello, how are you ? Today is 6 o’clock.“ Will be before encryption changed to OT = 
„HELLOXSPACEXHOWXSPACEXAREXSPACEXYOUXSPACEXXSPACEXTODAYXSPAC
EXISXSPACEXXSPACEXOCLOCK“ And after decryption I will obtain OT = „HELLO HOW 
ARE YOU TODAY IS OCLOCK“ with spaces as before encryptio

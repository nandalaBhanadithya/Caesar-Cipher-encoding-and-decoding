README

Problem: Caesar Cipher encoding and decoding

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 

For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence

Write code that implements encoding and decoding of a message.

The parameters for the methods would be the message to be encoded / decoded and the length of the shift.



Features

Encryption: Encode a plain text input using a configurable shift value.



Decryption: Decode an encrypted message, restoring the original plain text using the same shift value.



Configurable Shift: Works with any numerical shift value, both positive and negative.



Character Handling: Preserves case for letters and leaves non-alphabetic characters unchanged.



Getting Started

Prerequisites

Python 3.13.5



**Setup**

Clone the repository:



**bash**

git clone https://github.com/nandalaBhanadithya/Caesar-Cipher-encoding-and-decoding.git

cd Caesar-Cipher-encoding-and-decoding



**\[If required] Install dependencies:**



**bash**



pip install -r requirements.txt

Running the Code



To encrypt a message:



***bash***



python Caesar-Cipher-encoding-and-decoding.py --mode encrypt --shift 3 --text "Hello, World!"

To decrypt a message:



***bash***

python Caesar-Cipher-encoding-and-decoding.py --mode decrypt --shift 3 --text "Khoor, Zruog!"



**Arguments**

Argument	Description	Example

--mode	Mode: encrypt or decrypt	--mode encrypt

--shift	Shift value (integer)	--shift 4

--text	The message to encode or decode (in quotes)	--text "abc XYZ 123"





***Example***

***Encrypt:***



**text**

Input:  "OpenAI"

Shift:   2

Output: "QrpgCK"

Decrypt:



**text**

Input:  "QrpgCK"

Shift:   2

Output: "OpenAI"







Testing

Run the included test script to verify the implementation:



bash

python test\_caesar\_cipher\_encoding\_decoding.py

Files

Caesar-Cipher-encoding-and-decoding.py — Main implementation.



test\_caesar\_cipher.py — Unit tests.



README.md — Project documentation.



License

This project is submitted as part of the backend system assignment and is for educational and evaluation purposes only.



For assignment evaluators:

Please refer to assignments.md for the problem statement and verify solutions using the provided test cases and instructions.
















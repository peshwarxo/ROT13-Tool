#!/usr/bin/env python3
"""
ROT13 Encoder/Decoder Tool
Author: Your Name
Description: Simple Python script to perform ROT13 encoding and decoding on text.
"""

import codecs

def rot13(text: str) -> str:
    """Encodes/decodes text using ROT13 cipher."""
    return codecs.encode(text, 'rot_13')

def main():
    print("=== ROT13 Encoder/Decoder ===")
    while True:
        choice = input("\nEnter 'e' to encode, 'd' to decode, or 'q' to quit: ").lower()

        if choice == 'q':
            print("Goodbye!")
            break
        elif choice in ('e', 'd'):
            text = input("Enter your text: ")
            result = rot13(text)
            print(f"\nResult: {result}")
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()

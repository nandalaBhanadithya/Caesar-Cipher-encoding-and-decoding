def caesar_encode(message, shift):
    encoded = ''
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift letter and wrap around alphabet
            encoded += chr((ord(char) - base + shift) % 26 + base)
        else:
            encoded += char
    return encoded

def caesar_decode(encoded_message, shift):
    # Decoding is encoding with negative shift
    return caesar_encode(encoded_message, -shift)

if __name__ == "__main__":
    try:
        message = input("Enter message: ")
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for shift.")
        exit(1)
    encoded = caesar_encode(message, shift)
    print("Encoded:", encoded)
    decoded = caesar_decode(encoded, shift)
    print("Decoded:", decoded)

import unittest
from Caesar_Cipher_encoding_and_decoding import caesar_encode, caesar_decode  # Adjust import as needed

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_basic(self):
        self.assertEqual(caesar_encode("abc", 1), "bcd")

    def test_decrypt_basic(self):
        self.assertEqual(caesar_decode("bcd", 1), "abc")

    def test_encrypt_with_shift_zero(self):
        self.assertEqual(caesar_encode("hello", 0), "hello")

    def test_encrypt_wrap_around(self):
        self.assertEqual(caesar_encode("xyz", 3), "abc")

    def test_non_alpha_characters(self):
        self.assertEqual(caesar_encode("hello, world!", 5), "mjqqt, btwqi!")

if __name__ == "__main__":
    unittest.main()

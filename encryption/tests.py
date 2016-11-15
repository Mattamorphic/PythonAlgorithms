import unittest
import XorEncrypt

class TestEncryptionFunctions(unittest.TestCase):

    def test_xor_encrypt_works(self):
        plain = "Matt"
        key = "sup3rk3y"
        ciphered = XorEncrypt.encrypt(plain, key)
        self.assertEqual(plain, XorEncrypt.encrypt(ciphered, key))

    def test_xor_encrypt_invalid_key(self):
        plain = "Matt"
        key = "sup3rk3y"
        ciphered = XorEncrypt.encrypt(plain, key)
        self.assertNotEqual(plain, XorEncrypt.encrypt(ciphered, 'wrongkey'))


if __name__ == '__main__':
    unittest.main()

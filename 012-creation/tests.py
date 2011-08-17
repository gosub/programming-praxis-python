import unittest
import creation


class CreationTestCase(unittest.TestCase):
    def setUp(self):
        self.encrypted = creation.read_cipher("cipher_message.txt")
        self.decrypted = open("decipher_message.txt").read().rstrip('\n')
        self.password = "Genesis"

    def test_programming_praxis(self):
        "Verify found password length, found password and decrypted message. "
        passw_lens = creation.probable_password_lengths(self.encrypted)
        passw_len = passw_lens[0]
        self.assertTrue(passw_len % len(self.password) == 0)

        found_passw = creation.guess_password(self.encrypted, passw_len)
        possible_password_match = [self.password * i for i in [1, 2, 3]]
        self.assertIn(found_passw, possible_password_match)

        decrypt = creation.xor_crypt(self.encrypted, found_passw)
        self.assertEqual(self.decrypted, decrypt)


if __name__ == '__main__':
    unittest.main(verbosity=2)

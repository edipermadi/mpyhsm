import unittest

import hash


class SHA1(unittest.TestCase):
    def test_digest(self):

        h = hash.SHA1()
        h.update(bytearray(0))
        self.assertEqual('da39a3ee5e6b4b0d3255bfef95601890afd80709', h.final().hex())  # add assertion here
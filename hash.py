class SHA1:
    def __init__(self):
        self.__buffer = bytearray(64)
        self.__h0 = 0x67452301
        self.__h1 = 0xefcdab89
        self.__h2 = 0x98badcfe
        self.__h3 = 0x10325476
        self.__h4 = 0xc3d2e1f0

    def update(self, data):
        # 1 pad data to buffer
        for i in range(80):
            pass


    def final(self):
        return bytes()

    def __ch(self, x, y, z):
        return (x & y) ^ (~x & z)

    def __par(self, x, y, z):
        return x ^ y ^ z

    def __maj(self, x, y, z):
        return (x & y) ^ (x & y) ^ ( y & z)

import struct
import numpy as np
from codecs import decode
class BinaryHelper:
    @staticmethod
    def binary(num):
        return ''.join(bin(c).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))

    @staticmethod
    def floatVal(binaryString):
        sign = 1 if binaryString[0] == '0' else -1;
        rest = binaryString[1:]
        exponent = int(rest[0:8], 2) - 127
        bias = rest[8:]
        biasf = 1.0
        for i in range(len(bias)):
            if bias[i] == '1':
                biasf = biasf + 2**(-i-1)
        number = sign*biasf*(2**exponent)
        return number

    @staticmethod
    def bin_to_float(b):
        """ Convert binary string to a float. """
        print(int(b,2))
        bf = int.to_bytes(int(b, 2), 8, 'big')  # 8 bytes needed for IEEE 754 binary64.
        print(bf)
        return struct.unpack('>d', bf)[0]
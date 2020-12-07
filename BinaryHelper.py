import struct

class BinaryHelper:
    @staticmethod
    def binary(num):
        return ''.join(bin(c).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))

    @staticmethod
    def floatVal(binaryString):
        sign = 1 if binaryString[0] == '0' else -1
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
    def flipByte(byte):
        if(byte == '1'):
            return '0'
        elif (byte == '0'):
            return '1'

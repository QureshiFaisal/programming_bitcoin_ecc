class Signature:

    def __init__(self, r, s):
        self.r = r
        self.s = s

    def __repr__(self):
        return 'Signature({:x},{:x})'.format(self.r, self.s)
# end::source11[]

    def der(self):
        rbin = self.r.to_bytes(32, byteorder='big')
        # remove all null bytes at the beginning
        rbin = rbin.lstrip(b'\x00')
        # if rbin has a high bit, add a \x00
        if rbin[0] & 0x80:
            rbin = b'\x00' + rbin
        result = bytes([2, len(rbin)]) + rbin  # <1>
        sbin = self.s.to_bytes(32, byteorder='big')
        # remove all null bytes at the beginning
        sbin = sbin.lstrip(b'\x00')
        # if sbin has a high bit, add a \x00
        if sbin[0] & 0x80:
            sbin = b'\x00' + sbin
        result += bytes([2, len(sbin)]) + sbin
        return bytes([0x30, len(result)]) + result

    @classmethod
    def parse(cls, der_signature):
        if der_signature[0] != 0x30:
            raise ValueError("Invalid DER signature format")
        length = der_signature[1]
        if length + 2 != len(der_signature):
            raise ValueError("Invalid DER signature length")
        r_pos = 4
        r_length = der_signature[3]
        r = int.from_bytes(der_signature[r_pos:r_pos+r_length], 'big')
        s_pos = r_pos + r_length + 2
        s_length = der_signature[r_pos+r_length+1]
        s = int.from_bytes(der_signature[s_pos:s_pos+s_length], 'big')
        return cls(r, s)

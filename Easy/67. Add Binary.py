# v1

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]


# v2

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        if len_a >= len_b:
            return self.sumElements(a[::-1], b[::-1], len_b)
        else:
            return self.sumElements(b[::-1], a[::-1], len_a)

    def sumElements(self, long: str, short:str, len_short) -> str:
        lst_to_return = []
        trigger = False
        for idx, value in enumerate(long):
            if idx < len_short:
                if not trigger:
                    if (long[idx] == '1') and (short[idx] == '1'):
                        lst_to_return.append('0')
                        trigger = True
                    else:
                        lst_to_return.append(
                            str(int(long[idx]) + int(short[idx]))
                        )
                else:
                    if (long[idx] == '1') and (short[idx] == '1'):
                        lst_to_return.append('1')
                    elif (long[idx] == '1') or (short[idx] == '1'):
                        lst_to_return.append('0')
                    else:
                        lst_to_return.append('1')
                        trigger = False
            else:
                if not trigger:
                    lst_to_return.append(long[idx])
                else:
                    if long[idx] == '1':
                        lst_to_return.append('0')
                    else:
                        lst_to_return.append('1')
                        trigger = False
        if trigger:
            lst_to_return.append('1')
        return ''.join(lst_to_return[::-1])

# https://leetcode.com/problems/binary-watch/
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        solution = []
        value = 0
        while value < 2048 :
            new_bin = str(bin(value))[2:]
            if (new_bin).count('1') == turnedOn :
                new_bin = new_bin.zfill(10)
                hour = new_bin[:4]
                minu = new_bin[4:]
                if int(hour, 2) <= 11 \
                and int(minu, 2) <= 59 :
                    if int(minu, 2) < 10 :
                        solution.append(str(int(hour, 2))+':0'+str(int(minu, 2)))
                    else :
                        solution.append(str(int(hour, 2))+':'+str(int(minu, 2)))
            value += 1
        return list(set(solution))

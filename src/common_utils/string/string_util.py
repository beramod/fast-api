from datetime import datetime

class StringUtil:
    @classmethod
    def isBlank(cls, value):
        if value is None or len(value.strip()) == 0:
            return True
        else:
            return False

    @classmethod
    def parseInt(cls, value, default=0):
        return int(value) if value else default

    @classmethod
    def parseFloat(cls, value, default=0.0):
        return float(value) if value else default

    @classmethod
    def getDigit(cls, value):
        return ''.join([s for s in filter(str.isdigit, value)])

    @classmethod
    def makeIdByDtm(cls, idx=1, check=None):
        return check if check else datetime.now().strftime('%Y%m%d%H%M%S') + '_' + str(idx)

    @classmethod
    def split(cls, string, splitStr=','):
        arr = None

        if string:
            arr = string.split(splitStr)
            for idx in range(len(arr)):
                arr[idx] = arr[idx].strip()

        return arr

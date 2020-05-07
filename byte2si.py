import math


def main(byte):
    #byteの桁数を取得して、3桁刻みに単位を変えてくだけ
    if 0 <= byte:
        dig = int(math.log10(byte))
        if 0 <= dig < 3:
            bytes = byte / pow(10, 0)
            return bytes, 'B'
        elif 3 <= dig < 6:
            bytes = byte / pow(10, 3)
            return bytes, 'KB'
        elif 6 <= dig < 9:
            bytes = byte / pow(10, 6)
            return bytes, 'MB'
        elif 9 <= dig < 12:
            bytes = byte / pow(10, 9)
            return bytes, 'GB'
        elif 12 <= dig <= 15:
            bytes = byte / pow(10, 12)
            return bytes, 'TB'
    else:
        raise ValueError('Not num')


def byte2si(byte):
    num, unit = main(byte)
    #少数第2位まで丸める
    renum = round(num, 2)
    return str(renum) + unit

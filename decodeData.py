import base64

def decodeData(getStr):
    try:
        getData = b64decode(getStr)
    except TypeError:
        print "Base64 decode faild"
        exit(0)

    if !checkToken(getData)
       print "check Token errer"
       exit(0)
    
    PM = getData[0] + getData[1]*0x100
    try:     
        latitude = float(getData[4:15])
        longitude = float(getData[15:26])
    except ValueError:
        print "data type error"
        exit(0)
    return {"PM":PM, "latitude":latitude, "longitude":longitude}

def checkToken(getData):
    Data = getData[:-2]
    flag = 0
    token = 0
    for i in Data:
        if flag == 0:
            temp = ord(i)
            flag = 1
        else:
            temp *= 0x100
            temp += ord(i)
            token ^= temp
            temp = 0
            flag = 0
    if flag == 0:
        token ^= 0
    else:
        token ^= temp*0x100
        token ^= 0
    getToken = ord(getData[-2]) + ord(getData[-1])*0x100
    print hex(getToken)
    print hex(token)
    return getToken == token


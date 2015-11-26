from decodeData import *
from insertData import *
def getData():
    getStr = raw_input()
    data = decodeData(getStr)
    insertData(data)
    

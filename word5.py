#影音轉文字
#! python2
# -*- coding: UTF-8 -*-  
import requests  
import time  
import urllib  
import json  
import hashlib  
import base64  
  
URL = "http://api.xfyun.cn/v1/service/v1/iat"  
APPID = "5ade9bcc"  
API_KEY = "2a5c520ae43bfa103043f11740933ef3"  
  
def getHeader():  
    curTime = str(int(time.time()))  
    param = "{\"engine_type\": \"sms16k\", \"aue\": \"raw\"}"  
    paramBase64 = base64.b64encode(param)  
  
    m2 = hashlib.md5()  
    m2.update(API_KEY + curTime + paramBase64)  
    checkSum = m2.hexdigest()  
    header ={  
        'X-CurTime':curTime,  
        'X-Param':paramBase64,  
        'X-Appid':APPID,  
        'X-CheckSum':checkSum,  
        'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',  
    }  
    return header  
  
def main():  
    #filename = 'd:/python/545986818.872027.mp3'
    filename = '123.wav'
    f = open(filename, 'rb')  
    file_content = f.read()  
    base64_audio = base64.b64encode(file_content)  
    body = urllib.urlencode({'audio': base64_audio})  

    r = requests.post(URL,headers=getHeader(),data=body)  
    result = json.loads(r.content)  
  
    if result["code"] == "0":  
        print "success, data = " + result["data"]  
    else:  
        print r.text  
  
    return  
  
if __name__ == '__main__':  
    main()  
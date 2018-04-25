#! python2
#-*- coding: utf-8 -*-  
import requests  
import time  
import hashlib  
import base64  
  
URL = "http://api.xfyun.cn/v1/service/v1/tts"  
APPID = "5ade9bcc"  
API_KEY = "f24968286f853d6138ff1fda9f1bce10"  
def getHeader(auf, aue, voiceName, speed, volume, pitch, engineType, textType):  
    curTime = str(int(time.time()))  
    param = "{\"auf\":\""+auf+"\""  
    if aue != "":  
        param +=",\"aue\":\"" + aue + "\""  
  
    if voiceName != "":  
        param +=",\"voice_name\":\"" + voiceName + "\""  
  
    if speed != "":  
        param +=",\"speed\":\"" + speed + "\""  
  
    if volume != "":  
        param +=",\"volume\":\"" + volume + "\""  
  
    if pitch != "":  
        param +=",\"pitch\":\"" + pitch + "\""  
  
    if engineType != "":  
        param +=",\"engine_type\":\"" + engineType + "\""  
  
    if textType != "":  
        param +=",\"text_type\":\"" + textType + "\""  
  
    param +="}"  
  
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
  
def getBody(text):  
    data = {'text':text}  
    return data  
  
def writeFile(file, content):  
    with open(file, 'wb') as f:  
        f.write(content)  
    f.close()  
  
r = requests.post(URL,headers=getHeader("audio/L16;rate=16000", "raw", "xiaoyan", "50", "50", "50", "aisound", "text"),data=getBody("请输入你的身高和体重"))  
contentType = r.headers['Content-Type']  
if contentType == "audio/mpeg":  
    sid = r.headers['sid']  
    writeFile("audio/"+sid+".wav", r.content)  
    print "success, sid = " + sid  
else :  
    print r.text  
#!/usr/bin/python
#! python2
# -*- coding: UTF-8 -*-
import urllib2
import time
import urllib
import json
import hashlib
import base64


def main():
    api_key = '2a5c520ae43bfa103043f11740933ef3'
    x_appid = '5ade9bcc'
    #AUDIO_PATH = 'D:/python/545986818.872027.mp3'
    #AUDIO_PATH = 'D:/python/output.mp3'
    AUDIO_PATH = 'D:/python/123.wav'
    max_wanted_size = 1024 * 1024
    f = open(AUDIO_PATH, 'rb')
    file_content = f.read(max_wanted_size)
    base64_audio = base64.b64encode(file_content)
    body = urllib.urlencode({'audio': base64_audio})

    url = 'http://api.xfyun.cn/v1/service/v1/iat'
    param = {"engine_type": "sms16k", "aue": "raw"}

    x_param = base64.b64encode(json.dumps(param).replace(' ', ''))
    x_time = int(int(round(time.time() * 1000)) / 1000)
    x_checksum = hashlib.md5(api_key + str(x_time) + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum,
                'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',  
               }
    req = urllib2.Request(url, body, x_header)
    result = urllib2.urlopen(req)
    result = result.read()
    print result
    news = open('news.txt','wb')
    print(news.write(result))    
    return

if __name__ == '__main__':
    main() 
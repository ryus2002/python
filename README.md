# Python 小程式範例

## scrap1.py 
-> 爬蟲程式並將結果輸出至index.csv
-> 用法︰quote_page變數改成想要抓取的URL網址
```
quote_page = ['http://www.bloomberg.com/quote/SPX:IND', 'http://www.bloomberg.com/quote/CCMP:IND']
```

## tts.py、tts3.py 
-> 訊飛 文字轉音頻 WEB API
```
TEXT = "苟利国家生死以，岂因祸福避趋之"    #輸入想轉換的文字
OUTPUT_FILE = "d:/python/output.mp3"    #输出音频的保存路径，请根据自己的情况替换
```

## tts2.py 
-> 訊飛 文字轉音頻 SDK
需先安裝訊飛的SDK，參考網址︰https://www.xfyun.cn/sdk/dispatcher
```
text = "欢迎来到方工的CSDN博客。CSDN创立于1999年，是中国专业的IT技术社区和开发者服务平台。拥有5000万注册用户以及60万注册企业及合作伙伴。"  #輸入想轉換的文字
filename = "tts_sample.wav"  #输出音频的保存路径，请根据自己的情况替换
```

## word.py word5.py 
-> 訊飛 音頻轉文字 WEB API
-> 執行結果將顯示在螢幕上
```
filename = '123.wav' #音檔來源
```

## blockchain.py
##區塊練交易程式範例<br>
用法<br>
```
$ pipenv run python blockchain.py<br>
$ pipenv run python blockchain.py -p 5001<br>
$ pipenv run python blockchain.py --port 5002<br>
```

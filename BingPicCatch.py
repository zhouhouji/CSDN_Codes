import urllib.request
import re
import os.path

def saveImg(img_url,dirname):
    #保存图片到磁盘文件夹dirname中
    try:
        if not os.path.exists(dirname):
            print ('文件夹',dirname,'不存在，重新建立')
            #os.mkdir(dirname)
            os.makedirs(dirname)
        #获得图片文件名，包括后缀
        basename = os.path.basename(img_url)
        #拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        #下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url,filepath)
        print("Save", filepath, "successfully!")
    except IOError as e:
        print ('文件操作失败',e)
    except Exception as e:
        print ('错误 ：',e)
    return filepath

def getPage(url):
    #用于浏览器伪装
    headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    #获得网页源码并解码
    html_code = res.read().decode('UTF-8')
    return html_code

def main():
    url = 'https://bing.ioliu.cn/'
    #dirname='C:\Users\wzr\Desktop\srceen'
    html_code = getPage(url)
    #用于匹配网址的字符串
    pic_urls_match = r'data-progressive=\"(.*?)\"'
    image_urls = re.findall(pic_urls_match,html_code)
    for i in range (len(image_urls)):
        img_url = image_urls[i]
        filepath = saveImg(img_url,'C:\\Users\\wzr\\Desktop\\srceen')   # 图片文件的的路径
    print('Compelet')

if __name__ == '__main__':
    main()

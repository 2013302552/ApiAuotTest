'''
上传文件，一般都是post接口，用files参数上传文件
'''

import requests

url = "http://www.httpbin.org/post"

'''
files参数，字典的格式, 'name'：file-tuple
file-tuple可以是2-tuple('filename',fileobj)、3-tuple('filename',fileobj,'content_type')、4-tuple
'''
with open("d:/test.txt", encoding = 'utf-8') as f:
    # , "text/plain"如果上传的是一个文本文件，可以去掉content_type，默认文件类型是文本文件
    file = {"file1": ("test.txt", f, "text/plain")}  # MIME类型：text/plain、image/png、image/gif、application/json
    r = requests.post(url, files=file)
    print(r.text)
    # \u4e2d\u6587\u5b57 unicode编码的，
    # 上传一个图片，10k以内
with open("d:/fb0717.JPG",mode="rb") as n:
    file = {"file2": ("fb0717.JPG", n, 'image/jpg')}
    m = requests.post(url, files=file)
    print(m.text)
# with open("d:/FK123.PNG",mode="rb") as n:
#     file = {"file2": ("FK123.PNG", n, 'image/png')}
#     m = requests.post(url, files=file)
#     print(m.text)

# 可以一次上传多个文件

with open("d:/FK123.PNG",mode="rb") as l:
    with open("d:/test.txt", encoding = 'utf-8') as p:
        file = {"file1": ("test.txt", l , "text/plain") , "file2": ("fb0717.JPG", p , 'image/jpg')}
        k = requests.post(url,files = file)
        print(k.text)




from urllib import request

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

file = open("output.png", "wb")
file.write(output)
file.close()

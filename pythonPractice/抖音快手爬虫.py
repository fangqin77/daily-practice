url=""
import requests
res = requests.get(url)
print(res.status_code)
open("视频1.MP4","wb").write(res.content)
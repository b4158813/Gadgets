import requests 
from urllib import request
from lxml import etree

url = 'https://mp.weixin.qq.com/s/S2ga5wIFCR_uR1JKWUdx3Q'
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
}

try:
	r = requests.get(url,timeout=30,headers=headers)
	print('ye')
except:
	print('ooo')


r.encoding = 'utf-8' # 编码成utf-8才能正常读取中文

html = etree.HTML(r.text)
url = html.xpath("//img[@class='rich_pages']/@data-src")

print(url)

exit()
cnt=0
for ele in url:
	giao=request.Request(ele,headers=headers)
	res=request.urlopen(giao).read()
	cnt+=1
	with open("./emm/"+str(cnt)+".jpg","wb") as f:
		f.write(res)
		print("%d"%cnt)

print("finished")
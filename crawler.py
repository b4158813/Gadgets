import requests
from lxml import etree

def parse(url,headers,ans):
	r = requests.get(url, timeout=30, headers=headers)
	if r.status_code!=200:
		print("gg!\n")
		return
	# print(r.text)
	html = etree.HTML(r.text)
	html_data = html.xpath("//tbody//td[@class='jsk-hide-sm']/text()")
	
	temp=[]
	cnt=0
	# print(html_data)
	for ele in html_data:
		# print(ele)
		cnt+=1
		temp.append(ele.strip())
		# print(temp)
		if cnt==5:
			if temp[4]=='未开始':
				ans.append(temp)
				# print(ans)
			temp=[]
			cnt=0

	print(ans)
	# ans += html_data
	# print("第%s页爬取成功\n"%(url[-1]))



if __name__ == '__main__':

	ans = []

	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
	}

	# for i in range(1,2):
	# 	url = 'https://www.luogu.com.cn/problem/list?page='+str(i)
	url = 'https://nanti.jisuanke.com/contest'
	parse(url,headers,ans)

	# print(len(ans))
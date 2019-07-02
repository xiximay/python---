import requests							#requests是python实现的简单易用的HTTP库
import time
import csv 								#csv库主要用于处理csv文件
from pyquery import PyQuery as pq		#pyquery库可以用于解析HTML网页内容

number = 100
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,z;q=0.8'
    }
#定义一个函数，完成获取id功能
def get_id():
	url =  'http://www.zhigaokao.cn/university/getRemoteProvinceList.do?' #将网站的url即网址赋给url
	payload = {
			'userKey': 'www',
			'req': 'ajax',
		}
	response = requests.get(url, headers=headers, params=payload)#使用requests的get函数使用url访问网页
	items = response.json().get('bizData')#response返回json数据
	IDs = []#建立一个新列表
	for item in items:
		IDs.append(item.get('id'))#使用append函数依次向IDs列表中增加新元素
	return IDs#将IDs作为函数返回值返回
#定义一个函数，获取网页上的数据
def get_data(ID):
	url = 'http://www.zhigaokao.cn/university/getRemoteUniversityList.do?'#同上，将网页url赋给url变量
	#定义一个payload字典
	payload = {
			'userKey': 'www',
			'req': 'ajax',
			'areaid': ID,
			'educationLevel': 1,
			'offset': 0,
			'rows': 10
		}
	results = []#定义一个results列表
	length = 10
	while (payload['offset'] < number) and (length == 10):
		response = requests.get(url, headers=headers, params=payload)#使用requests的get函数使用url访问网页
		items = response.json().get('bizData').get('universityList')
		length = len(items)#获取items的长度
		payload['offset'] = payload['offset'] + length
		for item in items:
			results.append(item)
		time.sleep(1)#sleep函数用来延时
		print(payload['offset'])
	print_csv(results)
#定义打印csv文件函数
def print_csv(results):
	path = '.\province\\' + results[0].get('province') + '.csv'
	with open(path, 'w') as csvfile:#写入文件
		writer = csv.writer(csvfile, lineterminator='\n')
		for result in results:
			writer.writerow([result.get('name'), result.get('property')])
		print(path + ' finish!')
#主函数，用来调用get_id和get_data函数
def main():
	IDs = get_id()
	for ID in IDs:
		get_data(ID)
#运行主函数
if __name__ == '__main__' :
	main()

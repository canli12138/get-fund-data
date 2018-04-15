import os

class Setting:
	def __init__(self):
		self.url = "http://fund.eastmoney.com/"
		self.regex = 'gz_gszzl">[-+]\d+\.\d+%'
		self.url_path = os.path.join(os.getcwd(), 'fund.csv')
		self.result_path = os.path.join(os.getcwd(), 'result.csv')

	def get_url(self):
		fp = open(self.url_path, 'r', encoding='UTF-8')
		fund_code = fp.readlines()
		fp.close()
		code_list = []
		for line in fund_code:
			code_dict = {}
			code_dict[line.split(',')[0]] = self.url + line.split(',')[1].rstrip('\n') + '.html?spm=search'
			code_list.append(code_dict)		
		return code_list

if __name__ == '__main__':
	test = Setting()
	result = test.get_url()
	print(result)

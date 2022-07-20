import requests
from bs4 import BeautifulSoup
import json
import csv
import pprint
import re
import pandas as pd

class regexParser:
	def load_html(self, filename):
		html = ''
		with open(filename, 'r') as html_file:
			for line in html_file.read():
				html += line
		return html


	def parse(self, html):
		content = BeautifulSoup(html, "html.parser")
		block = content.find_all(attrs={"class": "g Ww4FFb tF2Cxc"})
		name_pos_companys = []
		for b in block:
			info = b.find(attrs={"class": "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"}).get_text()
			email = re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', info)
			if email:
				title = b.find(attrs={"class": "LC20lb MBeuO DKV0Md"}).get_text()
				title = title.split('-')
				print(title)

				if len(title) >= 1:
					name = title[0].strip()
				else: 
					name = ''
				if len(title) >= 2:
					pos = title[1].strip()
				else:
					pos = ''

				if len(title) >= 3:
					company = title[2].split('|')[0].strip()
				else:
					company = ''

				name_pos_company = {
					'name': name,
					'pos': pos,
					'company' : company,
					'email': email[0]
				}
				name_pos_companys.append(name_pos_company)
		return name_pos_companys


	def save_json_to_csv(self, name_pos_companys, filename_csv):
		df = pd.DataFrame(name_pos_companys)
		df.to_csv(filename_csv)
		# df.to_csv(filename_csv, mode='a', index=True, header=False)

	def run(self, filename, filename_csv):
		html = self.load_html(filename)
		name_pos_companys = self.parse(html)
		self.save_json_to_csv(name_pos_companys, filename_csv)



if __name__=='__main__':
	parser = regexParser()
	parser.run('temp.html', 'list_parser.csv')






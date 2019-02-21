import csv
import re
import datetime
from abc import ABC, abstractmethod
from lottery_util import wdcsv
#from imaplib import dat

def get_yesterday():
	"""
	得到前一天的信息
	"""
	today=datetime.date.today() 
	oneday=datetime.timedelta(days=1) 
	yesterday=today-oneday  
	return yesterday.strftime('%Y-%m-%d')

class BigCustomerTable():
	@property
	def filename(self):
		return 'BIGCUSTOMER.csv'
	@property
	def insert_sql(self):
		return "INSERT INTO SD_T_BIGCUSTOMER (CODE, NAME, SEND_PATTERN, TYPE, MANAGEMENT_CENTER, LINKMAN, PHONE, ADDRESS, EMS_CODE, STATES, MANAGE_DATE) VALUES "
	
	def get_data(self):
		print('getting BigCustomerTable Data')
		with open(wdcsv+self.filename) as f:
			reader = csv.reader(f)
			contents =[i for i in reader]
			date = get_yesterday()
			data = contents
		for i ,item in enumerate(data):
        		city_code = re.search("(\d+)",str(data[i][4])).group()
        		city_name = re.search("([\u4e00-\u9fa5]{2,4})",str(data[i][4])).group()
        		data[i].pop(4)
        		data[i].insert(4,city_code)
        		data[i].insert(5,city_name)
        		print(str(data[i]))
        		for j,item2 in enumerate(item):
        			if(j<=3):
        				continue
        			if(re.match('.*,.*',data[i][j],flags=0)):
        				data[i][j]=data[i][j].replace(',','')
		data_and_date = [i+[date] for i in data]
		print(str(data_and_date))
		return data_and_date


if __name__ == "__main__":
    a = BigCustomerTable()
    a.get_data()
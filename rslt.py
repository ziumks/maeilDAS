import time
import pymysql as sql
import random as r

conn = sql.connect(host='127.0.0.1', user='root', password='ziumks', db='maeil', charset='utf8')
qry = 'insert into monitoring_item_PD(deviceNo, time, Temp_R, Temp_S, Temp_T, PD) values(%s,%s,%s,%s,%s,%s);'

temp1 = r.randrange(260,270)/10
temp2 = r.randrange(260,270)/10
temp3 = r.randrange(260,270)/10
temp4 = r.randrange(260,270)/10
temp5 = r.randrange(260,270)/10
temp6 = r.randrange(260,270)/10
tmp1 = r.randrange(60,70)/10
tmp2 = r.randrange(60,70)/10
tmp3 = r.randrange(60,70)/10

def readPDTemp(num):
	registerPD = None
	registerTemp = None

	if num == 4:
		registerPD = 0
		registerTemp = temp1, temp2, temp3  		

	elif num == 5:
		registerPD = 0
		registerTemp = temp4, temp5, temp6

	elif num == 6:
		registerPD = 0
		registerTemp = tmp1, tmp2, tmp3
	else:
		print("system error!")
	param = num, round(time.time()), registerTemp[0], registerTemp[1], registerTemp[2], registerPD
	if not registerPD:
		if registerTemp:
			try:
				with conn.cursor() as cursor:
					cursor.execute(qry, param)
					conn.commit()
			except TypeError:
				print('connection error with Db. Check it.')
				pass
		else:
			print("reboot CAM-4 to get temperature")
	else:
		print("reboot CAM-4 to get PD")
	result = {'i':param[0], 'time': round(time.time()), 'Temp_R':param[2], 'Temp_S':param[3], 'Temp_T':param[4], 'PD':param[5]}
	return result

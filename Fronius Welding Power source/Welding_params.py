# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 07:42:45 2021

@author: dhruv
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 07:31:08 2021

@author: dhruv
"""

"""
Created on Tue Mar  9 16:55:23 2021

@author: dhruv
"""
from opcua import Client
from csv import writer


client = Client("opc.tcp://192.168.223.68:4840")
client.connect()
file1 = open("current.txt","a")
file2 = open("voltage.txt","a")
file3 = open("wfs.txt","a")


while True:
	
	var1 = client.get_node("ns=1;s=DISPLAY_CURRENT")
	var2 = client.get_node("ns=1;s=DISPLAY_VOLTAGE")
	var3 = client.get_node("ns=1;s=DISPLAY_WFS")
	var_1 = str(var1.get_value())
	var_2 = str(var2.get_value())
	var_3 = str(var3.get_value())
	
	with open('parameters.csv','a', newline='') as file:			
		writer_ob = writer(file)
		writer_ob.writerow([var_1,var_2,var_3])
			
	
	print("The Cuurent is", var_1)
	file1.writelines(var_1)
	print("The Voltage is", var_2)
	file2.writelines(var_2)
	print("The WFS is", var_3)
	file3.writelines(var_3)
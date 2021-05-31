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

client = Client("opc.tcp://192.168.223.68:4840")
client.connect()
file1 = open("current.txt","w")
file2 = open("voltage.txt","w")
file3 = open("wfs.txt","w")

while True:
	var1 = client.get_node("ns=1;s=DISPLAY_CURRENT")
	var2 = client.get_node("ns=1;s=DISPLAY_VOLTAGE")
	var3 = client.get_node("ns=1;s=DISPLAY_WFS")
	var_1 = var1.get_value()
	var_2 = var2.get_value()
	var_3 = var3.get_value()
	
	print("The Cuurent is", var_1)
	file1.write("var_1")
	print("The Voltage is", var_2)
	file1.write("var_2")
	print("The WFS is", var_3)
	file1.write("var_3")
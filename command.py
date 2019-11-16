import os
import subprocess
from tkinter import *


cmd = [ "iverilog", "-o", "temp", "temp.v" ]
rn = ["vvp", "temp"]

def compile(code, log):
	string =  code.get("1.0", "end-1c")
	file = open("temp.v", "w")
	file.write(string)
	file.close()

	output,error = subprocess.Popen(cmd,stdout = subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	log.config(state=NORMAL)
 	log.insert(END,error)
 	log.insert(END, output)
 	log.config(state=DISABLED)

def run(log):
	output,error = subprocess.Popen(rn,stdout = subprocess.PIPE, stderr=subprocess.PIPE, shell = "true").communicate()
	log.config(state=NORMAL)
	log.insert(END,error)
	log.insert(END, output)
 	log.config(state=DISABLED)


	
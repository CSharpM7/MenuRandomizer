import os
import os.path
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import sys
import shutil


inputFolder = os.getcwd() + "/input"
outputFolder = os.getcwd() + "/output"
template = os.getcwd() + "/template"
nus3Path = "/stream;/sound/bgm/"
clonename = "/bgm_crs2_01_menu.nus3audio"
clonebank = "/bgm_crs2_01_menu.nus3bank"

for file in os.listdir(inputFolder):
	if file.endswith(".nus3audio"):
		filename = os.path.basename(file)
		foldername = filename.replace(".nus3audio","")
		filebank = file.replace(".nus3audio",".nus3bank")
		targetDir = outputFolder+"/"+foldername
		if (not os.path.exists(targetDir)):
			shutil.copytree(template,targetDir)
		nus3Location = targetDir+nus3Path
		#Remove files first
		for f in os.listdir(nus3Location):
			os.remove(os.path.join(nus3Location, f))
		#Clone
		shutil.copy(os.path.join(inputFolder,file),nus3Location+clonename)
		shutil.copy(os.path.join(inputFolder,filebank),nus3Location+clonebank)
		print(targetDir)


messagebox.showinfo("Message Box","Finished!")
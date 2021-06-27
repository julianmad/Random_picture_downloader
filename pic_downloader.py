from datetime import datetime
import requests
import shutil
import os


url = "https://random.imagecdn.app/500/150"
date = datetime.now().strftime('Date_%Y-%m-%d_Time_%H-%M-%S')
file = date+ "_" + url.split("/")[-1] + ".jpg"

opn = requests.get(url, stream = True)
if opn.status_code == 200:
	opn.raw.decode_content = True
	dir_img = "./Randompics"
	dir_res = os.path.exists(dir_img)
	if (dir_res==False):
		os.makedirs(dir_img)
	else:
		print("Given directory already exists! \n")	
			
	with open("Randompics/" + file, 'wb') as f:
		shutil.copyfileobj(opn.raw, f)
	print("Image sucessfully downloaded!", file)
	
else: 
	print("Problem mate")



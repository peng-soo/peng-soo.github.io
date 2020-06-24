from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]
for fileName in onlyfiles :
	print("<div onclick='onClick(this)'><img src='" + fileName + "'><span><br><input type='text' value='http://peng-soo.github.io/" + fileName + "'></span></div>")
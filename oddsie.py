from sys import argv
import subprocess
print("ODDSIE (c) 2022 LFWJ")
def trans(name):
	i_f=open(name)
	o_f=open(name.replace(".od","")+".py","w")
	o_l=[]
	l_t=0
	l_n=1
	print("PROCESS: Starting lexing of "+i_f.name+"...")
	for line in i_f:
		l_i=""
		l_t=int(l_t)
		line=line.replace("\n","")
		tokens=line.replace("\t","").split(".")
		if tokens[0]=="end":
			l_t-=1
			print("KEYWORD FOUND: END")
		elif tokens[0]=="define":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"def "+tokens[1])
			print("KEYWORD FOUND: DEFINE")
		elif tokens[0]=="die":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"quit()")
			print("KEYWORD FOUND: DIE")
		elif tokens[0]=="display":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"print("+tokens[1].replace(",,",".")+")")
			print("KEYWORD FOUND: DISPLAY")
		elif tokens[0]=="do":
			for i in range(l_t):l_i=l_i+"\t"
			try:o_l.append(l_i+tokens[1]+"("+tokens[2].replace(",,",".")+")")
			except IndexError:o_l.append(l_i+tokens[1]+"()")
			print("KEYWORD FOUND: DO")
		elif tokens[0]=="ifot":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"elif "+tokens[1])
			print("KEYWORD FOUND: IFOT")
		elif tokens[0]=="otherwise:":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"else:")
			print("KEYWORD FOUND: OTHERWISE")
		elif tokens[0]=="if":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"if "+tokens[1])
			print("KEYWORD FOUND: IF")
		elif tokens[0]=="for":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"for "+tokens[1]+tokens[2])
			print("KEYWORD FOUND: FOR")
		elif tokens[0]=="use":
			o_l.append("import "+tokens[1])
			print("KEYWORD FOUND: USE")
		elif tokens[0]=="var":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+tokens[1].replace(",,",".")
			print("KEYWORD FOUND: VAR")
		elif tokens[0]==";" or tokens[0]=="//":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"#"+tokens[1].replace(",,","."))
			print("KEYWORD FOUND: COMMENT")
		elif tokens[0]=="set":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append("class "+tokens[1])
			print("KEYWORD FOUND: SET")
		elif tokens[0]=="through":
			o_l.append("from "+tokens[1]+" import "+tokens[2])
			print("KEYWORD FOUND: THROUGH")
		elif tokens[0]=="nothing":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"pass")
			print("KEYWORD FOUND: NOTHING")
		elif tokens[0]=="attempt:":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"try:")
			print("KEYWORD FOUND: ATTEMPT")
		elif tokens[0]=="error:":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"except:")
			print("KEYWORD FOUND: ERROR")
		elif tokens[0]=="give":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"return "+tokens[1])
		else:print("WARNING: No keywords detected at line "+str(l_n))
		if line.endswith(":"):l_t+=1
		l_n+=1
	print("Done")
	print("PROCESS: Starting to write translation to "+o_f.name+"...")
	i=1
	for item in o_l:
		print("LINE WRITTEN: "+str(i))
		o_f.write(item+"\n")
		i+=1
	print("Done")
	return o_f.name
if argv[1]=="help":
	print("oddsie [option] [file]")
	print("OPTIONS")
	print("help\t\t\tBrings up this menu.")
	print("transpile\t\tTranspiles [file] into python from Oddsie.")
	print("keywords\tShows list of Oddsie keywords.")
elif argv[1]=="keywords":
	print("define,die,display,do,ifot,otherwise,end,if,for,use,var,set,through,nothing,give")
elif argv[1]=="transpile":
	trans(argv[2])
elif argv[1]=="pyinstaller":
	subprocess.run("pysintaller "+trans(argv[2]),shell=True)
else:
	trans(argv[1])

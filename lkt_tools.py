import os
os.system('clear')
os.system("figlet LKT-TOOLS")
print('''

\033[0;33m|--------------------*--------------------|
		 LKT-TOOLS
\033[0;33m|--------------------*--------------------|				


'''.center(40))

print('''
  \033[0;31m[ 01 ] \033[0;32mShow all tools. [ Almost 373 tools ]
  \033[0;31m[ 02 ]\033[0;32m Install Library Python.
 \033[0;31m [ 03 ] \033[0;32mAbout LKT-TOOLS.
 \033[0;31m [ 00 ]\033[0;32m For Exit.

'''.center(40))

while True:
	select_oprtion=input("~> ")
	if select_oprtion =="1":
		os.system('clear')
		os.system("figlet LKT-TOOLS")
		print('''
		
\033[0;33m|--------------------*--------------------|
	     Selcet your tool
\033[0;33m|--------------------*--------------------|				
	


 \033[0;32m[ 1 ] \033[0;33minstall \033[0;32mpython
 \033[0;32m[ 2 ] \033[0;33minstall \033[0;32mruby
 \033[0;32m[ 3 ] \033[0;33minstall \033[0;32mphp
 \033[0;32m[ 4 ] \033[0;33minstall \033[0;32mghost
 \033[0;32m[ 5 ] \033[0;33minstall \033[0;32msaycheese
 \033[0;32m[ 6 ] \033[0;33minstall \033[0;32mosif
 \033[0;32m[ 7 ] \033[0;33minstall \033[0;32msudo
 \033[0;32m[ 8 ] \033[0;33minstall \033[0;32mT-Header
 \033[0;32m[ 9 ] \033[0;33minstall \033[0;32mfiglet
 \033[0;32m[ 10 ] \033[0;33minstall \033[0;32mnano
 \033[0;32m[ 11 ] \033[0;33minstall \033[0;32mreport-fb
 
 
		
		
		''')
		
		select_tool=input("~> ")
		if select_tool == "0":
			print("good bye ^-^")
			break
		elif select_tool =="1":
			os.system('clear')
			print('''
		
\033[0;33m|--------------------*--------------------|
	     Installing
\033[0;33m|--------------------*--------------------|''')
		
			print(" \033[0;33mWait Install Python ...")
			os.system("pkg install python")
			break
			print("Done !")
		elif select_tool =="2":
			os.system('clear')
			print('''
		
\033[0;33m|--------------------*--------------------|
	     Installing
\033[0;33m|--------------------*--------------------|''')
			print(" \033[0;33mWait Install Ruby ...")
			os.system("pkg install Ruby")
			break
			print("Done !")
		elif select_tool =="3":
			os.system('clear')
			print('''
		
\033[0;33m|--------------------*--------------------|
	     Installing
\033[0;33m|--------------------*--------------------|''')
			print(" \033[0;33mWait Install PHP ...")
			os.system("pkg install php")
			break
			print("Done !")
			
		elif select_tool =="4":
			os.system('clear')
			print('''
		
\033[0;33m|--------------------*--------------------|
	     Installing
\033[0;33m|--------------------*--------------------|''')
			print(" \033[0;33mWait Install GHOST ...")
			
			os.system("git clone https://github.com/TryGhost/Ghost")
		
			break
			print("Done !")
		elif select_tool =="5":
			os.system('clear')
			print('''
		
\033[0;33m|--------------------*--------------------|
	     Installing
\033[0;33m|--------------------*--------------------|''')
			print(" \033[0;33mWait Install SAYCHEESE ...")
			
			os.system("https://github.com/hangetzzu/saycheese")
		
			break
			print("Done !")
		elif select_tool =="6":
			os.system('clear')
			print('''
		
\033[0;33m|--------------------*--------------------|
	     Installing
\033[0;33m|--------------------*--------------------|''')
			print(" \033[0;33mWait Install OSIF ...")
			
			os.system("git clone https://github.com/ciku370/OSIF")
		
			break
			print("Done !")
		elif select_tool =="7":
			os.system('clear')
			print('''
		
\033[0;33m|--------------------*--------------------|
	     Installing
\033[0;33m|--------------------*--------------------|''')
			print(" \033[0;33mWait Install SUDO ...")
			os.system("pkg install tsu ")
			os.system("pkg install ncurses-utils ")
			os.system("git clone https://gitlab.com/st42/termux-sudo.git​")
		
			break
			print("Done !")
		elif select_tool =="8":
			os.system('clear')
			print('''
		
\033[0;33m|--------------------*--------------------|
	     Installing
\033[0;33m|--------------------*--------------------|''')
			print(" \033[0;33mWait Install HEADER ...")
			os.system("git clone https://github.com/remo7777/T-Header.git​")
		
			break
			print("Done !")
		elif select_tool =="9":
			os.system('clear')
			print('''
		
\033[0;33m|--------------------*--------------------|
	     Installing
\033[0;33m|--------------------*--------------------|''')
			print(" \033[0;33mWait Install FIGLET ...")
			os.system("pkg install figlet")
		
			break
			print("Done !")
		elif select_tool =="10":
			os.system('clear')
			print('''
		
\033[0;33m|--------------------*--------------------|
	     Installing
\033[0;33m|--------------------*--------------------|''')
			print(" \033[0;33mWait Install NANO ...")
			os.system("pkg install nano")
		
			break
			print("Done !")
		elif select_tool =="11":
			os.system('clear')
			print('''
		
\033[0;33m|--------------------*--------------------|
	     Installing
\033[0;33m|--------------------*--------------------|''')
			print(" \033[0;33mWait Install report-fb ...")
			os.system("https://github.com/hekelpro/report-fb")
		
			break
			print("Done !")


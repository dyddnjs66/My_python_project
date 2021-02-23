#-*- coding:utf-8 -*-
# Code by Yebin
#Discord:이예빈#1924, Telegram:yblee ,Email:yblee0816@naver.com
from bs4 import BeautifulSoup
from urllib.request import urlopen

import os

cmd = 'mode 48,29'
os.system(cmd) # 창 버퍼 조절!
while True:
     print('\033[96m'+"Code by Yebin made only to fun\n"+'\033[96m')
     print('\033[96m'+"Telegram:yblee\nEmail:yblee0816@naver.com"+'\033[96m')
     print('\033[96m'+"Discord:이예빈#1924\n"+'\033[96m')

     input_ip=input('\033[96m'+"Target ip: "+'\033[96m')

     response=urlopen("https://findip.opendocs.co.kr/exe/process?ip_address="+input_ip)
     soup=BeautifulSoup(response, 'html.parser')

     ip=soup.select("#infobox > div > p:nth-child(2)")
     code=soup.select("#infobox > div > p:nth-child(3)")

     if ip[0].text==">  IP 유형 : IPv4":
          print("┌"+"─"*19+"┐")
          print("│",ip[0].text,"│") #ip 설명 긁어오기
          print("│",code[0].text," │") #나라 설명 긁어오기
          print("└","─"*17,"┘","\n")

          user=soup.select("#infobox > div > div:nth-child(8) > p.subtitle")
          sub_user=soup.select("#infobox > div > div:nth-child(8) > p:nth-child(2)")

          print(user[0].text)
          print(sub_user[0].text)
     else:
          print("존재하지 않는 IP 이거나 IPv6입니다.\n")

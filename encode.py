import base64
import platform
import os
import re
import time
try:
  import pyfiglet
except:
  os.system('pip install pyfiglet')
  
# Coded By Mr.SaMI
red = "\033[1;31m"
green = "\033[1;32m"
cyan = "\033[1;36m"

def clear():
  if platform.system() == "Windows":
    os.system("cls")
  else:
    os.system("clear")

def banner():
  sami = pyfiglet.Figlet(font="slant")
  banner = sami.renderText("ENCODING HTML")
  print(f"""{green}
                       Coded By Mr.SaMi : @TYG_YE
                            Version : V 1.0
""")
  print(f"{red}{banner}")

def main():
    clear()
    print(f"{cyan}[{red}0%{cyan}]{green}")
    time.sleep(0.5)
    clear()
    print(f"{cyan}[{red}10%{cyan}]{green}■")
    time.sleep(0.5)
    clear()
    print(f"{cyan}[{red}20%{cyan}]{green}■■")
    time.sleep(0.5)
    clear()
    print(f"{cyan}[{red}30%{cyan}]{green}■■■")
    time.sleep(0.5)
    clear()
    print(f"{cyan}[{red}40%{cyan}]{green}■■■■")
    time.sleep(0.5)
    clear()
    print(f"{cyan}[{red}50%{cyan}]{green}■■■■■")
    time.sleep(0.5)
    clear()
    print(f"{cyan}[{red}60%{cyan}]{green}■■■■■■")
    time.sleep(0.5)
    clear()
    print(f"{cyan}[{red}70%{cyan}]{green}■■■■■■■")
    time.sleep(0.5)
    clear()
    print(f"{cyan}[{red}80%{cyan}]{green}■■■■■■■■")
    time.sleep(0.5)
    clear()
    print(f"{cyan}[{red}90%{cyan}]{green}■■■■■■■■■")
    time.sleep(0.5)
    clear()
    print(f"{cyan}[{red}100%{cyan}]{green}■■■■■■■■■■")
    clear()
    banner()
    html = input(f'{cyan}[!]{green} Enter your html file {cyan}---> {red}')
    code = open(html,'r',encoding='UTF-8').read()
    text = code.encode('utf-8')
    bsen = base64.b64encode(text).decode('utf-8')
    html_encoding =f"""
<!-- Encoding By Mr.SaMi | Telegram : t.me/TYG_YE -->
<!-- GitHub :  https://github.com/mr-sami-x -->
<script type='text/javascript'>document.documentElement.innerHTML=atob('{bsen}');</script>
"""
    
    path = os.getcwd()
    open(f"{html.replace('.html','')}_en.html",'w').write(f'{html_encoding}')
    time.sleep(1)
    clear()
    print(f"{cyan}[{red}0%{cyan}]{green}")
    time.sleep(1)
    clear()
    print(f"{cyan}[{red}10%{cyan}]{green}■")
    time.sleep(1)
    clear()
    print(f"{cyan}[{red}20%{cyan}]{green}■■")
    time.sleep(1)
    clear()
    print(f"{cyan}[{red}30%{cyan}]{green}■■■")
    time.sleep(1)
    clear()
    print(f"{cyan}[{red}40%{cyan}]{green}■■■■")
    time.sleep(1)
    clear()
    print(f"{cyan}[{red}50%{cyan}]{green}■■■■■")
    time.sleep(1)
    clear()
    print(f"{cyan}[{red}60%{cyan}]{green}■■■■■■")
    time.sleep(1)
    clear()
    print(f"{cyan}[{red}70%{cyan}]{green}■■■■■■■")
    time.sleep(1)
    clear()
    print(f"{cyan}[{red}80%{cyan}]{green}■■■■■■■■")
    time.sleep(1)
    clear()
    print(f"{cyan}[{red}90%{cyan}]{green}■■■■■■■■■")
    time.sleep(1)
    clear()
    print(f"{cyan}[{red}100%{cyan}]{green}■■■■■■■■■■")
    clear()
    banner()
    print(f"{cyan}[+]{red} The file was encrypted and saved as:‍{green} {path}\{html.replace('.html','')}_en.html")

main()

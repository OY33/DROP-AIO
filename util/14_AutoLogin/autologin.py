import os, time, os.path
from colorama import Fore
from util.plugins.commun import * 

def autologin() :
    from selenium import webdriver
    setTitle("Auto Login")
    clear()
    autologintitle()
    print(f"""{y}[{w}+{y}]{w} Enter the token of the account you want to connect to""")
    entertoken = str(input(f"""{y}[{b}#{y}]{w} Token: """))
    try:
        driver = webdriver.Chrome(executable_path=r'util/chromedriver.exe')
        driver.maximize_window()
        driver.get('https://discord.com/login')
        js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
        time.sleep(3)
        driver.execute_script(js + f'login("{entertoken}")')
        time.sleep(10)
        if driver.current_url == 'https://discord.com/login':
            clear()
            autologintitle()
            print(f"""{y}[{Fore.LIGHTRED_EX }!{y}]{w} Connection Failed""")
            driver.close()
        else:
            clear()
            autologintitle()
            print(f"""{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Connection Established""")
        input(f"""{y}[{b}#{y}]{w} Press ENTER to exit""")
        main()
    except:
        print(f"""      {y}[{Fore.LIGHTRED_EX }!{y}]{w} There is a problem with your Token""")
        time.sleep(2)
        clear()
        main()

autologin()

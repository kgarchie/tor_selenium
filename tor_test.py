from selenium import webdriver
import os
import time
from stem.control import Controller
from stem import Signal
from stem import process

# To use Tor's SOCKS proxy server with chrome, include the socks protocol in the scheme with the --proxy-server option
# PROXY = "socks5://127.0.0.1:9150" # IP:PORT or HOST:PORT

while True:
    try:
        tor_launcher = process.launch_tor_with_config(
          config = {
            'ControlPort': '9051',
            },
        )
    except OSError:
        print("Please terminate the running tor process in task manager(optional), Press Ctrl+C to stop the program")
        raise

# torexe = os.popen(r'C:\Users\Kuski\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
PROXY = "socks5://127.0.0.1:9050" # IP:PORT or HOST:PORT
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(options=options, executable_path=r'path\to\chromedriver.exe')
driver.get("http://www.icanhazip.com")
time.sleep(5)


with Controller.from_port(port=9051) as controller:
    controller.authenticate()
    print("successful authenticate")
    controller.signal(Signal.NEWNYM)
    
driver.get("http://www.icanhazip.com")
time.sleep(5)
tor_launcher.terminate()
driver.quit()   


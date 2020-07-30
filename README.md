# tor_sellenium

This is a simple working python program that changes your IP address each time you connect

## Getting started
To install on Windows machines with python already installed correctly
  1. open powershell/terminal
  2. change directory to your preferred directory *unnecessary*
  3. type `mkdir tor_tests`
  4. then cd into it using `cd tor_tests`
  5. create a virtual environment `python -m venv myvenv`
  6. activate it using `myvenv/Scripts/activate` *Note the S is capital*
  
Now we laugh HAHAHA
## More requirements(*for those who know what they are doing start here*)
You need Tor(if you don't know what that is, i hope you are enjoying your retirement)
Download it from [here](https://www.torproject.org/download/)

Install the requirements for the file to run as specified in [requirements.exe](https://github.com/kgarchie/tor_selenium/blob/master/requirements.txt)

After Stem is installed we need to fix a bug
  - go to (*the relative path is*)`myvenv/Lib/site-packages/stem` and edit the stem file called process.py on line 204
  it reads by default
  ```python
  def launch_tor_with_config(config, tor_cmd = 'tor', completion_percent = 100, init_msg_handler = None, timeout = DEFAULT_INIT_TIMEOUT, take_ownership = False, close_output = True):
  # the rest of the code
    pass
  ```
  - change it to
   ```python
   def launch_tor_with_config(config, tor_cmd = 'where_you_installed_your_tor_browser\\Tor Browser\\Browser\\TorBrowser\\Tor\\tor.exe', completion_percent = 100, init_msg_handler = None, timeout = DEFAULT_INIT_TIMEOUT, take_ownership = False, close_output = True):
   # PS make sure it directs to tor.exe wherever the hell it is in your system
    pass
   ```

You need ChromeWebdriver from [here](https://chromedriver.chromium.org/downloads)*i used chrome i'm either too lazy to dig around other browsers or inept*

You need to know what you are doing

run the file using `python tor_tests.py`

i've just given you power beyond your imagination **With great power comes great responsibility**

for errors i'll be happy to help just leave a comment

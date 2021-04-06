# tor_sellenium

This is a simple working python program that changes your IP address each time you connect

## Getting started

* open powershell/terminal as administrator(this will help us deal with some issues that may arise)
* change directory to your preferred directory (unnecessary, just note the current directory so that you don't lose your files) Use  ```cd``` to change directory eg ```cd desktop``` will change the working directory to the desktop which I can recommend as it is easy to find the files later.
* type ```mkdir tor_tests``` We are making a directory named 'Project', but you can call it whatever you want.
* then cd into it using the command ```tor_tests``` (this makes it the current working directory)
* create a virtual environment ```python -m venv myvenv```(this creates a virtual environment for python)
* activate the environment using ```myvenv/Scripts/activate``` (Note the S is capital). You may receive an error because running scripts is disabled. At this point restart powershell this time as administrator and type in this command 'set-executionpolicy remotesigned'. It will allow local scripts to run.

Now we laugh HAHAHA
### More requirements
You need Tor
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

You need ChromeWebdriver from [here](https://chromedriver.chromium.org/downloads) *i used chrome i'm either too lazy to dig around other browsers or inept*

You need to know what you are doing

run the file using `python tor_tests.py`

i've just given you power beyond your imagination **With great power comes great responsibility** seriously tho use it wisely, I won't be responsible if you end up in prison

for errors i'll be happy to help just raise ann issue or pull request

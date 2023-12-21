# CBTracker (CollegeBoard Tracker)

So this is the repo, with script that Logins, and proceeds to page where you can see all Test Centers available in your country. 

## Note 0
The account must prepared for usage with the script. Also after sometime account may be blocked, do not use you primary account. It won't register for you, it only messages you the available places. Also your IP may get blocked after sometime, especially when new dates open. <br>
~~You may need to correct this script with correct XPATH-es because I'm no longer maintaining this script, and CollegeBoard periodically changes website structures.~~ <br>
Bot no longer uses XPATH, rather it uses elements' ID-s. I update them from time to time.

## Note 1
~~I kindly ask you to ignore the bot token in `tgmessage.py`, bot is dead anyways, the id is leftover anyways, especially considering that it will be available in commits history anyways.~~ <br>
There are bot tokens there, but I kindly ask you not use them. Otherwise I'm just gonna block the bot. Please change it. I use this repository as transfer system between my computer and the server, so i can just reboot my server and get changes there directly.

## How to use
- Install Selenium:  
`pip install selenium`

<del>- If you want to use without Xorg running you must install `xvfb` for your distribution and `xvfbwrapper` from pip.</del> Headless mode doesn't work well. I no longer use Xvfb, rather i start up Xorg session with i3, since I have VNC there.


- Change Bot token in `tgmessage.py` to token of your bot, and put your chat ID in your bot.
  To find find chat id, proceed to `https://api.telegram.org/bot{BOTTOKEN}/getUpdates`(replace {BOTTOKEN} with your token, such as `https://api.telegram.org/bot6056379592:BAHd_dsfkjwlkfnskdnfwoeirfhlknflwkU7w/getUpdates`, and send message to your bot, then refresh the api webpage, you'll find ID in json presented by API.

- Change email and password in `main.py` at line 180. 

- And at last run `main.py` script. 

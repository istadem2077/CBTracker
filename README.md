# CBTracker (CollegeBoard Tracker)

So this is the repo, with script that Logins, and proceeds to page where you can see all Test Centers available in you country. 

## Note 0
The account must prepared for usage with the script. Also after sometime account may be blocked, do not use you primary account. It won't register for you, it only messages you the available places. Also if your IP may get blocked after sometime, especially when new dates open. 
You may need to correct this script with correct XPATH-es because I'm no longer maintaining this script, and CollegeBoard periodically changes website structures. 

## Note 1
I kindly ask you to ignore the bot token in `tgmessage.py`, bot is dead anyways, the id is leftover anyways, especially considering that it will be available in commits history anyways. 

## How to use
- Install Selenium:  
`pip install selenium`

- If you want to use without Xorg running you must install `xvfb` for your distribution and `xvfbwrapper` from pip. Headless mode doesn't work well.
    And add this after last import:  
    ```python
    from xvfbwrapper import Xvfb
    
    vdisplay = Xvfb(width=1920, height=1080)
    vdisplay.start()
    ```
    and at the very end of the script:
    ```python
    vdisplay.stop()
    ```

- Change Bot token in `tgmessage.py` to token of your bot, and put your chat ID in your bot.
  To find find chat id, proceed to `https://api.telegram.org/bot{BOTTOKEN}/getUpdates`(replace {BOTTOKEN} with your token, such as `https://api.telegram.org/bot6056379592:BAHd_dsfkjwlkfnskdnfwoeirfhlknflwkU7w/getUpdates`, and send message to your bot, then refresh the api webpage, you'll find ID in json presented by API.

- Change email and password in `main.py` at line 180. 

- And at last run `main.py` script. 

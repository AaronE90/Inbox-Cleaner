import os
import sys
import email
import time
import socket
import imaplib
import getpass

from pyfiglet import Figlet
from colorama import Fore, Back, Style, init

RED = Fore.RED
RESET = Fore.RESET
MAGENTA = Fore.MAGENTA
YELLOW = Fore.YELLOW
WHITE = Fore.WHITE
CYAN = Fore.CYAN
S_BRIGHT = Style.BRIGHT

today = time.asctime()
fig = Figlet(font='standard')


banner = f'''{S_BRIGHT}{MAGENTA}
                      __________________
                      \                 \\
                        \                 \\
                          \                 \\
                            \                 \\
           /-------------------------------------
         //---------------//                  / |
       //               //                  / __|
     //               //                  / /  ||
   //               //                  / /    ||
 //_______________//   o o            / /      ||      ___/-\___
------------------------------------/   ------- |     |---------|
| {CYAN}DO NOT PLAY {MAGENTA}|         | {CYAN}HOUSEHOLD {MAGENTA}|           |      | | | | |
| {CYAN}ON OR AROUND{MAGENTA}|         |{CYAN}WASTE ONLY {MAGENTA}|           |      | | | | |
|--------------         ------------|           |      | | | | |
|                                   |           |      | | | | |
-------------------------------------------------      |_______|
            {YELLOW}{today}{CYAN}

'''

def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
Clear()


print(banner)
print(fig.renderText(f'Inbox Clean-Up'))
username = input(f'{S_BRIGHT}{MAGENTA}Please enter email address{WHITE}: {CYAN}')
print('')
password = getpass.getpass(f'{S_BRIGHT}{MAGENTA}Please enter password{WHITE}: {CYAN}')
print('')
print(f'{S_BRIGHT}{MAGENTA}Signing into {CYAN}{username}{MAGENTA} account.')

def main():
    try:
        imap = imaplib.IMAP4_SSL('imap.gmail.com', 993, timeout=5)
        print(f'{S_BRIGHT}{MAGENTA}Connecting...')
        imap.login(username, password)
        imap.select('INBOX', readonly=False)

        status, messages = imap.search(None, 'ALL')
        messages = messages[0].split(b' ')
        print(f'{S_BRIGHT}{MAGENTA}Getting ready to clean. May take a few minutes...')

        for mail in messages:
            _, msg = imap.fetch(mail, "(RFC822)")
            imap.store(mail, "+FLAGS", "\\Deleted")

        print(f'{S_BRIGHT}{MAGENTA}Cleaning everything now{WHITE}...')
        imap.expunge()
        print(f'{S_BRIGHT}{MAGENTA}Exiting mailbox folder{WHITE}...')
        imap.close()
        print(f'{S_BRIGHT}{MAGENTA}Logging out of account{WHITE}...')
        imap.logout()
        print(f'{S_BRIGHT}{MAGENTA}Thanks 4 Using {WHITE}:{CYAN})')

    except Exception as e:
        print(f'{S_BRIGHT}{RED}[OOPS]{WHITE}:{YELLOW} Something went wrong.{RESET}')
        print(f'{S_BRIGHT}{YELLOW}{e}{RESET}')

if __name__ == '__main__':
    main()

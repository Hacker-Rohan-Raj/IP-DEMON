import colorama
from colorama import Fore, Back, Style
from ip2geotools.databases.noncommercial import DbIpCity

print(Fore.CYAN, Back.BLACK + '''
     
                                                                       .         .                                            
 8 8888 8 888888888o   8 888888888o.      8 8888888888            ,8.       ,8.           ,o888888o.     b.             8 
 8 8888 8 8888    `88. 8 8888    `^888.   8 8888                 ,888.     ,888.       . 8888     `88.   888o.          8 
 8 8888 8 8888     `88 8 8888        `88. 8 8888                .`8888.   .`8888.     ,8 8888       `8b  Y88888o.       8 
 8 8888 8 8888     ,88 8 8888         `88 8 8888               ,8.`8888. ,8.`8888.    88 8888        `8b .`Y888888o.    8 
 8 8888 8 8888.   ,88' 8 8888          88 8 888888888888      ,8'8.`8888,8^8.`8888.   88 8888         88 8o. `Y888888o. 8 
 8 8888 8 888888888P'  8 8888          88 8 8888             ,8' `8.`8888' `8.`8888.  88 8888         88 8`Y8o. `Y88888o8 
 8 8888 8 8888         8 8888         ,88 8 8888            ,8'   `8.`88'   `8.`8888. 88 8888        ,8P 8   `Y8o. `Y8888 
 8 8888 8 8888         8 8888        ,88' 8 8888           ,8'     `8.`'     `8.`8888.`8 8888       ,8P  8      `Y8o. `Y8 
 8 8888 8 8888         8 8888    ,o88P'   8 8888          ,8'       `8        `8.`8888.` 8888     ,88'   8         `Y8o.` 
 8 8888 8 8888         8 888888888P'      8 888888888888 ,8'         `         `8.`8888.  `8888888P'     8            `Yo 

''')
print(Fore.RED, Back.BLACK + '''
     
     .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
''')
print(Fore.GREEN + 'Made By Hacker--Rohan Raj')
print(Fore.YELLOW + 'IP DEMON--Get Information of Any IP ADDRESS')
ipaddrofuser =  input('Please Enter Your IP Address')

response = DbIpCity.get(ipaddrofuser, api_key='free')
print('Your IP Adddress  ' + response.ip_address)
print('Your City  ' + response.city)
print('Your Region  ' + response.region)
print('Your Country  ' + response.country)
print(response.to_json())
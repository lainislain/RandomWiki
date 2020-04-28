import requests
from os import system as cmd

S = requests.Session()

limit = 7

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "generator": "random",
    "grnlimit": str(limit),
    "grnnamespace": "0",
    "prop": "info",
    "inprop": "url"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

RANDOMS = DATA["query"]["pages"]

checkn = 0
i = 1

for k in RANDOMS:
    if checkn == 1 :
        break
    print("\nYour lucky wiki is : " + RANDOMS[k]["title"] + "\n")
    x = 'n'
    while x != 'y' and checkn == 0 :
        x = input("Do you want another random wiki-page (y/n) ?   ")
        if x == 'y' :
            i += 1
            break
        elif x == 'n':            
            print("Have a good reading!")
            cmd("firefox " + RANDOMS[k]["fullurl"])
            checkn = 1
            break
        else:
            print("Wrong input! Try again..")
if i >= limit and x != 'n':
    print("Sorry, you reached the limit.. please restart the program.")
import requests
import random
import sys

tld_ = str(None)
i = int(0)
uri = str(None)
usedURI = []
domainsFound = []
HELP_ = False

uriGen = 'abcdefghijklmnopqrstuvwxyz1234567890'

if len(sys.argv) > 1:
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        HELP_ = True
        print('\n#py domain-miner.py [URI Length] [Top Level Domain]\n')

if len(sys.argv) > 1 and HELP_ == False:
    uriLen = sys.argv[1]
else:
    uriLen = int(input('Length of URI: '))

if len(sys.argv) > 2 and HELP_ == False:
    tld_ = sys.argv[2]
else:
    tld_ = str(input('Top Level Domain: '))

try:
    timeout_ = int(input("Reply timeout (s): "))
except KeyboardInterrupt:
    print("\n\nTerminating script\n")
    exit()
except:
    timeout_ = 1

possibleDomains = 36**int(uriLen)

print(f"\nScanning for {possibleDomains:,} domains\n")

while possibleDomains > len(usedURI):
    try:
        uri = 'https://'
        while i < int(uriLen):
            uri += random.choice(uriGen)
            i += 1
        uri += tld_
        if uri in usedURI:
            pass
        else:
            x = requests.get(uri, headers={'user-agent': 'domain-miner'}, timeout=timeout_)
            print(f'Domain {uri} returned staus code {x.status_code}')
            usedURI.append(uri)
            domainsFound.append(uri)
    except KeyboardInterrupt:
        print("\nTerminating script\n")
        print(f"{len(domainsFound):,}/{len(usedURI):,} Domains Found: {domainsFound}\n")
        exit()
    except Exception as e:
        print(f'{uri} Not Found')
        usedURI.append(uri)
    uri = None
    i = 0

print(f"Done!\n\n{len(domainsFound):,}/{possibleDomains:,} Domains Found: {domainsFound}")
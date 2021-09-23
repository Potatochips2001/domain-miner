#!/usr/bin/env python3
from requests import get
from random import choice
from sys import argv

#Defines
activeDomains = []
scannedDomains = []
selectFrom = '1234567890qwertyuiopasdfghjklzxcvbnm'
httpMethod = 0
_arg = ''

try:
  if argv[1] == '--silent':
    _arg = 'silent'
except:
  pass

class Main:
  def scanHTTP(uri: str, method, _timeout):
    if method != 1 and method != 2:
      print('Method not accepted!')
      exit()
    if method == 1:
      try:
        httpGet = get(uri, timeout=_timeout, headers={'user-agent': 'domain-miner'})
      except KeyboardInterrupt:
        print('\nTerminating script...\n')
        try: f = int(len(activeDomains) / len(scannedDomains) * 1000) / 10
        except: f = 0
        print(f'\nScanned {len(activeDomains)} / {len(scannedDomains)} ({f}%)\n')
        print(f'\n{activeDomains}\n')
        exit()
      except:
        return False
      if httpGet.text != '':
        print(f'{uri} => {httpGet.url} - {httpGet}')
        return True
      if httpGet.text == '':
        return False
    if method == 2:
      try:
        httpGet = get(uri, timeout=_timeout, headers={'user-agent': 'domain-miner'})
        print(f'{uri} => {httpGet.url} - {httpGet}')
        return True
      except KeyboardInterrupt:
        print('\nTerminating script...\n')
        try: f = int(len(activeDomains) / len(scannedDomains) * 1000) / 10
        except: f = 0
        print(f'\nScanned {len(activeDomains)} / {len(scannedDomains)} ({f}%)\n')
        print(f'\n{activeDomains}\n')
        exit()
      except:
        return False

  def silentScanHTTP(uri: str, method, _timeout):
    if method != 1 and method != 2:
      print('Method not accepted!')
      exit()
    if method == 1:
      try:
        httpGet = get(uri, timeout=_timeout, headers={'user-agent': 'domain-miner'})
      except KeyboardInterrupt:
        print('\nTerminating script...\n')
        try: f = int(len(activeDomains) / len(scannedDomains) * 1000) / 10
        except: f = 0
        print(f'\nScanned {len(activeDomains)} / {len(scannedDomains)} ({f}%)\n')
        print(f'\n{activeDomains}\n')
        exit()
      except:
        return False

  def genURI(n, method, topld):
    current = ''
    if method != 1 and method != 2:
      print('Method not accepted!')
      exit()
    if method == 1: current = 'http://'
    if method == 2: current = 'https://'
    for i in range(n):
      current += choice(selectFrom)
    return current + topld

if __name__ == '__main__':
  #Variables
  httpMethod = int(input('1) HTTP - Checks for empty response\n2) HTTPS\n'))
  uriLength = int(input('URI Length: '))
  tld = input('Top level domain: ')
  _timeout = float(input('Timeout (s): '))
  possibleDomains = 36**uriLength
  print(f'Scaning for {possibleDomains:,} domains')
  #start
  while _arg != 'silent':
    if len(scannedDomains) == possibleDomains:
      try: f = int(len(activeDomains) / len(scannedDomains) * 1000) / 10
      except: f = 0
      print(f'\nDone! Scanned {len(activeDomains)} / {len(scannedDomains)} ({f}%)\n')
      exit()
    try:
      uri = Main.genURI(uriLength, httpMethod, tld)
      while uri in scannedDomains:
        uri = Main.genURI(uriLength, httpMethod, tld)
      r = Main.scanHTTP(uri, httpMethod, _timeout)
      scannedDomains.append(uri)
      if r == True:
        activeDomains.append(uri)
      if r == False:
        print(f'{uri} - Not Found!')
    except KeyboardInterrupt:
      print('\nTerminating script...\n')
      try: f = int(len(activeDomains) / len(scannedDomains) * 1000) / 10
      except: f = 0
      print(f'\nScanned {len(activeDomains)} / {len(scannedDomains)} ({f}%)\n')
      print(f'\n{activeDomains}\n')
      exit()
    except Exception as e:
      pass
  while _arg == 'silent':
    if len(scannedDomains) == possibleDomains:
      try: f = int(len(activeDomains) / len(scannedDomains) * 1000) / 10
      except: f = 0
      print(f'\nDone! Scanned {len(activeDomains)} / {len(scannedDomains)} ({f}%)\n')
      exit()
    try:
      uri = Main.genURI(uriLength, httpMethod, tld)
      while uri in scannedDomains:
        uri = Main.genURI(uriLength, httpMethod, _timeout)
      r = Main.silentScanHTTP(uri, httpMethod, _timeout)
      scannedDomains.append(uri)
      if r == True:
        activeDomains.append(uri)
    except Exception as e:
      print(e)
    print(f'\rScanned {len(activeDomains)} / {len(scannedDomains)} domains', end='')
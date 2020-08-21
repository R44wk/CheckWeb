import sys
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

if len(sys.argv)==2:
    target = Request(sys.argv[1])
    try:
        response = urlopen(target)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print ('Website is working fine')
else:
    print("""
    HELP!
    Givme an argument, Example:
    #python3 CheckWeb.py httpe://www.any-site.com
    """)
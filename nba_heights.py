import urllib.request, json, sys, signal

def signal_handler(sig, frame):
    sys.exit(0)

'Reading argument:'
try:
    adds_up = int(sys.argv[1])
except:
    print('Please specify an integer to find the matching pair of players...')
    sys.exit(0)

'Retriving data:'
url = "https://mach-eight.uc.r.appspot.com/"
print('\nRetrieving Data...\n')
data = None
while data is None:
    try:
        data = urllib.request.urlopen(url).read().decode()
    except:
        print('The site "https://mach-eight.uc.r.appspot.com/" is not available. Press Enter to try again. CTRL-C to exit...')
        signal.signal(signal.SIGINT, signal_handler)
        input()
info = json.loads(data)

'finding:'
find = [x[0] for x in [[info['values'][i]['first_name'] + ' ' + info['values'][i]['last_name'] + '\t\t' + info['values'][j]['first_name'] + ' ' + info['values'][j]['last_name'] for j in range(i+1, len(info['values'])) if (int(info['values'][i]['h_in']) + int(info['values'][j]['h_in']) == adds_up)] for i in range(len(info['values']))] if len(x) > 0]

if (len(find) == 0): print('No matches found...')
else:
    for x in find: print(x)

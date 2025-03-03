# The Universal Terminal
# Created By: Phil H.
# Github: https://github.com/MineFartS/Universal-Terminal/

version = 'Beta 1.11'

last_updated = '2025-02-28'

#=======================================================#
#                   Startup Tasks                       #
#=======================================================#

try:
    import subprocess, sys, os, time, requests
except:
    import subprocess,sys,os
    subprocess.call([sys.executable,'-m','pip','install'])

# [dash] - Print dashes to a % of the terminal window 
def dash(percent=100,pad=False):
    dash = int(os.get_terminal_size().columns * percent/100) * '-'
    if pad: print('\n'+dash+'\n')
    else: print(dash)

# Print script title if initial start
os.system({False:'clear',True:'cls'}[os.name == 'nt'])
dash()
print("\nThe Universal Terminal ("+str(version)+")\n")
dash()

all_commands = []
help_commands = []

# OS type (Windows, Unix)
OS = {True:'Windows',False:'Unix'}[os.name == 'nt']

# OS Slash Type (\, /)
Slash = {'Windows':'\\','Unix':'/'}[OS]

# Path with current script file
ScriptPath = sys.path[0] + Slash + sys.argv[0]

#=======================================================#
#                  Terminal Commands                    #
#=======================================================#

def main(Input):
    cmd = Input.split(' ')[0]
    args = Input[Input.find(' '):]

    # [about] - Displays details about this script *Fixed
    params = ['about','ver','info']
    if cmd in params:        
        dash(40)
        print('The Universal Terminal')
        print('Created by Phil H.')
        dash(40)
        print('Version:',str(version))
        dash(20)
        print('Last Updated:',last_updated)
        dash(20)
        print('Github: "https://github.com/minefarts/universal-terminal"')
        dash(40)

    # [Clear] - Clears the terminal window *Fixed
    params = ['cls','clear']
    if cmd in params:
        os.system({False:'clear',True:'cls'}[os.name == 'nt'])

    # [Exit] - Exit Terminal *Fixed
    params = ['exit','quit','leave','end','close','return','throw']
    if cmd in params:
        exit()

    # [update] - Updates the script form GitHub
    params = ['update']
    if cmd in params:
        print('Fetching latest version from github ... ')
        code = requests.get('https://raw.githubusercontent.com/MineFartS/Universal-Terminal/refs/heads/main/run.py').text
        print('Applying Update ... ')
        cwd = os.getcwd()
        os.chdir(sys.path[0])
        open(sys.argv[0],'w').write(code)
        print('Update Complete')
        os.chdir(cwd)

    # [os] - Runs commands with the computer's default terminal *Fixed
    params = ['run','os','terminal','term','cmd','bash']
    if cmd in params:
        os.system(args)

    # [echo] - Echoes text back
    params = ['echo','say','repeat','write','text','print']
    if cmd in params:
        "'echo [text]' - writes text to the console\n'echo [text]>[file]' - writes text to a file"
        if '>' in input:
            text, file = args.split('>')
            open(file,'a').write('\n'+text)
        else:
            print(args)

    # [wait] - Waits for a certain number of seconds *Fixed
    params = ['wait','timeout','sleep','hold']
    if cmd in params:
        'wait [seconds]\nwait'
        t = 1
        print('Waiting ...')
        while t < int(args)+1:
            print(t)
            time.sleep(1)
            t += 1

    # [call] - Runs List of commands from text file
    params = ['call','script','execute']
    if cmd in params:
        for line in open(args,'r+').read().splitlines():
            '' # Fix

    # [delete] - Delete file or directory 
    params = ['delete','rm','del','remove']
    if cmd in params:
        try:
            os.remove(args)
        except:
            os.removedirs(args)

    # [pause] - Pauses session 
    params = ['pause','stop','halt','freeze']
    if cmd in params:
        if OS == "Windows":
            os.system("pause")
        else:
            os.system("read -n 1 -s -p 'Press any key to continue . . . '")

    # [python] - Runs Python 
    params = ['python','py3','py','python3']
    if cmd in params:
        
        args = [sys.executable]
        for p in params[1:]:
            args.append(p)
        subprocess.call(args)

    # [pip] - Runs Pip 
    params = ['pip','pip3']
    if cmd in params:
        
        args = [sys.executable,'-m','pip']
        for p in params[1:]:
            args.append(p)
        subprocess.call(args)

    # [ping] - ping command 
    params = ['ping']
    if cmd in params:
        if '-n' in args:
            c = int(args.split('-n')[1])
        if '-c' in args:
            c = int(args.split('-c')[1])
        if not '-n' in args or '-c' in args:
            c = 4
        if OS=='Windows':
            os.system('ping -n '+c+' '+params[1])
        else:
            os.system('ping -c '+c+' '+params[1])

    # [download] - download web page/file to disk 
    params = ['download','wget','get','web','request','save']
    if cmd in params:
        
        open(params[2],'wb').write(requests.get(params[1]).content)

    # [cd] - Change Directory 
    params = ['cd']
    if cmd in params:
        
        os.chdir(args.replace({'\\':'/','/':'\\'}[Slash],Slash))

    # [list] - List Directory Contents 
    params = ['list','dir','ls']
    if cmd in params:
        print('')
        items = []
        for path in os.listdir(os.getcwd()):
            if os.path.isdir(path):
                items.append('1[ Folder ] '+path)
            if os.path.isfile(path):
                items.append('2[  File  ] '+path)
        items.sort()
        for item in items:
            print(item[1:])

    # ['mkdir] - Make Directory 
    params = ['mkdir']
    if cmd in params:
        os.makedirs(os.getcwd()+Slash+args+Slash)

    # [help] - Display Help Message 
    params = ['help','/?','-h','-help','?','h','-?']
    if cmd in params:
        if len(Input.split(' ')) == 1:
            dash(15,True)
            print("Commands:\n")
            help_commands.sort()
            print(str(help_commands)[1:-1].replace("'",'').replace(', ','\n'))
            dash(15,True)
            print('Try Running "help [command]" for more detailed information')
            print('Note: While in beta, some commands might not have help options')
            dash(15,True)
            print('Some commands have alternatine phrase')
            print('Try running "[command] -alt" to list them')
            dash(15,True)

    # To Do: Fix Params Dual Error Message
    # open in text file editor, use cmd output as input, variables (%var%, etc)

while 0 < 1:
    text = input('\n'+os.getcwd()+' > ')
    for i in text.split('&&'):
        try:
            main(i)
        except:
            print('')
            dash(50)
            print('Error: Invalid Syntax or Command')
            print('Run "help" for a list of Commands')
            dash(25)
            print('Please share any glitches or bugs on github')
            print('https://github.com/MineFartS/Universal-Terminal/')
            dash(50)
print('There was an error. Please restart the terminal.')

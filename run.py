# Phil's Universal Terminal
# Github: https://github.com/MineFartS/Universal-Terminal/

version = 'Beta '+str(1.5)

last_updated = '2025-02-28'

#========================================================

#========================================================
#               Startup Handlers
#          (and some early functions):

try:
    import subprocess, sys, os, time, requests
except:
    import subprocess,sys,os
    repos = []

    args = [sys.executable,'-m','pip','install']
    for repo in repos:
        args.append(repos)
    subprocess.call(args)

# Function to restart the script
Allow_Restart = True
def restart(parameters=[]):
    if Allow_Restart:
        args = [sys.executable, sys.argv[0], '--restart']
        for p in parameters: args.append(p)
        subprocess.call(args)
        exit()
    else:
        exit()

def dash(percent=100,pad=False):
    x = 0
    dash = ''
    while x < os.get_terminal_size().columns*[percent/100][0]:
        dash += '-'
        x += 1
    if pad: print('\n'+dash+'\n')
    else: print(dash)
    return dash

# Check if session restarted
params = sys.argv[1:999]

if not '--restart' in params and not '--hidden-exec' in params:
    # Print Script Title
    os.system('cls' if os.name == 'nt' else 'clear')
    dash()
    print("\nThe Universal Terminal ("+str(version)+")\n")
    dash()

remove_args = ['--restart','--hidden-exec','--display-help-message','--list-phrases']

for arg in remove_args:
    if arg in params:
        params.remove(arg)

# Ask for parameters input if none passed through OS's CL
if len(params) == 0:
    params = input('\nUniversal Terminal \\> ').split(' ')
else:
    if not '--restart' in sys.argv: Allow_Restart = False

#========================================================

#========================================================
#               Global Variables:

all_commands = []
help_commands = []

# Get OS type (Windows/Unix)
OS = {True:'Windows',False:'Unix'}[os.name == 'nt']

ScriptPath = sys.path[0] + {'Windows':'\\','Unix':'/'}[OS] + sys.argv[0]

#========================================================
#               Functions for Commands To Call:

# Simplifies the process of creating new commands
def Param(names,index=0):
    if '--list-phrases' in sys.argv:
        if params[0] in names:
            print('\nAlternative commands for "'+params[0]+'":\n'+ListifyArray(names))
            restart()        
    help_commands.append(names[0])
    for name in names:
        all_commands.append(name)
        if name.capitalize() == params[index].capitalize(): return True
    return False

# Gets a range of Parameters as plain text
def ParamText(min=1,max=999):
    return str(params[min:max]).replace('[','').replace(']','').replace("'",'').replace(',','')

# Run command in os terminal
def terminal(command):
    if OS == 'Windows':
        subprocess.Popen('cmd /c ' + command)
    else:
        os.system(command)

# Pause session
def Pause():
    if OS == "Windows":
        os.system("pause")
    else:
        os.system("read -n 1 -s -p 'Press any key to continue . . . '")

# Get next parameter from parameter
def NextParam(parameter):
    return params[params.index(parameter)+1]

def GetPathInput(start=1):
    try:
        return ParamText(start,999).split('"')[1]
    except:
        return ParamText(1,999)
    
def help(message):
    if '--display-help-message' in sys.argv:
        print(message)
        restart()

def ListifyArray(array):
    return str(array)[1:-1].replace("'",'').replace(', ','\n')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def command(parameters=[]):
    args = [sys.executable, sys.argv[0],'--hidden-exec']
    for p in parameters:
        args.append(str(p))
    subprocess.call(args)

#========================================================

#========================================================
#               Terminal Commands:

if '&&' in params:
    cmds = ParamText(0).split('&&')
    for c in cmds:
        args = [sys.executable, sys.argv[0],'--hidden-exec']
        parts = c.split(' ')
        for part in parts:
            if not part == '': args.append(part)
        subprocess.call(args)
    restart()

# [about] - Displays details about this script
if Param(['about','ver']):
    dash(40)
    print('The Universal Terminal')
    print('A simple terminal for all users and platforms')
    dash(40)
    print('Version:',str(version))
    dash(20)
    print('Last Updated:',last_updated)
    dash(20)
    print('Created by Phil H.')
    dash(20)
    print('Github: "https://github.com/minefarts/universal-terminal"')
    dash(40)

# [Clear] - Clears the terminal window
if Param(['cls','clear'],0):
    clear()

# [Exit] - Exit with certain parameters
if Param(['exit','quit','leave','end','close','exit()','return'],0):
    Allow_Restart = False

# [Update] - Updates the script form GitHub
if Param(['update']):
    print('Fetching latest version from github ... ')
    code = requests.get('https://raw.githubusercontent.com/MineFartS/Universal-Terminal/refs/heads/main/run.py').text
    print('Applying Update ... ')
    open(sys.argv[0],'w').write(code)
    print('Update Complete')

# [os] - Runs commands with the computer's default terminal
# Run command in OS's terminal
if Param(['run','os','terminal','term','cmd','bash'],0):
    terminal(ParamText(1,999))

# [echo] - Echoes text back
if Param(['echo','say','repeat','write','text'],0):
    help(
"""Two Methods:
'echo [text]' - writes text to the console
'echo "[text]">[file]' - writes text to a file
""")
    input = ParamText(1,999)
    if '>' in input:
        text, file = input.split('>')
        open(file,'a').write('\n'+text.split('"')[1])
    else:
        print(input)

# [wait] - Waits for a certain # of seconds
if Param(['wait','timeout','sleep','hold'],0):
    x = 1
    y = int(params[1])
    while x < y+1:
        if '--hide' not in params:
            print(x,'of',y,'seconds')
        time.sleep(1)
        x += 1

# [call] - Runs List of commands from text file
if Param(['call','script','execute']):
    file = GetPathInput(1)
    for line in open(file,'r+').read().splitlines():
        args = [sys.executable, sys.argv[0],'--hidden-exec']
        for part in line.replace('\n','').split(' '):
            args.append(part)
        subprocess.call(args)
        if '-pause' in params:
            Pause()

# [delete] - Delete file or directory
if Param(['delete','rm','del','remove'],0):
    help('delete [file|folder]')
    if '"' in ParamText():
        path = ParamText().split('"')[1]
    else:
        path = ParamText()
    try:
        os.remove(path)
    except:
        os.removedirs(path)

# [pause] - Pauses session
if Param(['pause','stop','halt','freeze']):
    Pause()

# [python] - Runs Python
if Param(['python','py3','py','python3']):
    args = [sys.executable]
    for p in params[1:]:
        args.append(p)
    subprocess.call(args)

# [pip] - Runs Pip
if Param(['pip','pip3']):
    args = [sys.executable,'-m','pip']
    for p in params[1:]:
        args.append(p)
    subprocess.call(args)

# [cd] - Change Directory
if Param(['cd']):
    restart()
    #Unfinished -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    dir = GetPathInput()
    print(dir)
    if OS == 'Windows':
        os.system('cd /d '+dir)
    else:
        os.system('cd '+dir)

# List Directory Contents
if Param(['list','dir','ls']):
    restart()
    #Unfinished -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    if OS == 'Windows':
        os.system("echo Current Directory: %cd%")
        dash(15)
        os.system('dir')
    else:
        os.system('echo Current Directory: ')
        dash(15)
        os.system('ls')

# Add shortcut to system32, etc.
if Param(['AddToPath']):
    restart()
    #Unfinished -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    if OS=='Windows':
        terminal('copy "'+ScriptPath+'"'+file+'"C:\\Windows\\System32\\UnivTerm.py"')
        file = open('C:\\Windows\\System32\\UT.bat','w').write('python UnivTerm.py')

if Param(['ping']):
    if '-n' in params:
        count = NextParam('-n')
        params.remove('-n')
        params.remove(count)
    else:
        count = '4'
    if OS=='Windows':
        terminal('ping -n '+count+' '+params[1])
    else:
        terminal('ping -c '+count+' '+params[1])

if Param(['power']):
    restart()
    #Unfinished -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    if '-t' in params:
        time = int(NextParam('-t'))
        params.remove('-t')
    else:
        time = 30
    power = {'off':0,'on':1,'restart':2, 'abort':3}[params[1]]
    print(power)
    command(['wait',time])
    if params[0]==1:
        ""

if Param(['wget','download']):
    print(ParamText())
    input = ParamText().split('"')[1:4]
    
    r = requests.get(input[0])
    with open(input[2],'wb') as f:
        f.write(requests.content)

# To Do: create file, create dir, edit file, open file, wget, shutdown/restart (power), cd, addToPath, list, use cmd output as input

#========================================================

#========================================================
#                   Help Message

if Param(['help','/?','-h','-help','?','Help'],0):
    if len(params) == 1: 
        dash(15,True)
        print("Commands:\n")
        print(ListifyArray(help_commands))
        dash(15,True)
        print('Try Running "help [command]" for more detailed information')
        print('Note: While in beta, some commands might not have help options, any may error if run')
        dash(15,True)
        print('Some commands have alternatine phrase')
        print('Try running "help -alt [command]" to list them')
        dash(15,True)
        restart()
    else:
        if Param(['-alt','-list','-phrases','-other'],1):
            restart([params[2],'--list-phrases'])
        else:
            restart([params[1],'--display-help-message'])

#========================================================

#========================================================
#                   Handle Restart

if not params[0] in all_commands:
    print('')
    dash(50)
    print('Error: Invalid Syntax or Command')
    print('Run "help" for a list of Commands')
    dash(50)
    restart()
else: restart()
#========================================================

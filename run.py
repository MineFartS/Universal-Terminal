# Phil's Universal Terminal
# Github: https://github.com/MineFartS/Universal-Terminal/

version = 'Beta '+str(1.3)

last_updated = '2025-02-28'

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

def dash(percent=100,doPrint=True):
    x = 0
    dash = ''
    while x < os.get_terminal_size().columns*[percent/100][0]:
        dash += '-'
        x += 1
    if doPrint: print(dash)
    return dash

# Check if session restarted
params = sys.argv[1:999]
if '--restart' in params:
    params.remove('--restart')
else:
    if '--hidden-exec' in params:
        params.remove('--hidden-exec')
    else:
        # Print Script Title
        os.system('cls' if os.name == 'nt' else 'clear')

        dash()
        print("\nThe Universal Terminal (v"+str(version)+")\n")
        dash()

# Ask for parameters input if none passed through OS's CL
if len(params) == 0:
    params = input('Universal Terminal > ').split(' ')
else:
    if not '--restart' in sys.argv: Allow_Restart = False

all_commands = []

# Function to simplify the process of creating new commands
def Param(names,index=0):
    for name in names:
        all_commands.append(name)
        if name.capitalize() == params[index].capitalize(): return True
    return False

# Gets a range of Parameters as plain text
def ParamText(min,max):
    return str(params[min:max]).replace('[','').replace(']','').replace("'",'').replace(',','')

# Get OS type (Windows/Unix)
OS = {True:'Windows',False:'Unix'}[os.name == 'nt']

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


# Clears the terminal window
if Param(['cls','clear'],0):
    os.system('cls' if os.name == 'nt' else 'clear')

# Exit with certain parameters
if Param(['exit','quit','leave','end','close','exit()','return'],0):
    Allow_Restart = False

if Param(['update']):
    print('Fetching latest version from github ... ')
    code = requests.get('https://raw.githubusercontent.com/MineFartS/Universal-Terminal/refs/heads/main/run.py').text
    print('Applying Update ... ')
    open(sys.argv[0],'w').write(code)
    print('Update Complete')

# Show help options if run with 'help' parameter
if Param(['help','/?','-h','-help','?','Help'],0):
    print("** Help Message Will Go Here **")

# Run command in OS's terminal
if Param(['os','terminal','term','cmd','bash'],0):
    terminal(ParamText(1,999))

# echo
if Param(['echo','say','repeat'],0):
    input = ParamText(1,999)
    if '>' in input:
        text, file = input.split()
    print(input.split('>')[0])

# Waits for a certain # of seconds
if Param(['timeout','wait','sleep','hold'],0):
    x = 1
    y = int(params[1])
    while x < y+1:
        if '--hide' not in params:
            print(x,'of',y,'seconds')
        time.sleep(1)
        x += 1

# Run text file with list of commands for this terminal (like a batch file)
if Param(['script','call','run','execute']):
    file = GetPathInput(1)
    for line in open(file,'r+').read().splitlines():
        args = [sys.executable, sys.argv[0],'--hidden-exec']
        for part in line.replace('\n','').split(' '): # Fix \\ ------------
            args.append(part)
        subprocess.call(args)
        if '-pause' in params:
            Pause()

# Delete file or folder
if Param(['del','rm','delete','remove','wipe'],0):
    path = ParamText(1,999).split('"')[1]
    try:
        os.remove(path)
    except:
        os.removedirs(path)

# Pause
if Param(['pause','stop','halt','freeze']):
    Pause()

# Python
if Param(['py','py3','python','python3']):
    args = [sys.executable]
    for p in params[1:]:
        args.append(p)
    subprocess.call(args)

# Pip
if Param(['pip','pip3']):
    args = [sys.executable,'-m','pip']
    for p in params[1:]:
        args.append(p)
    subprocess.call(args)

# Change Directory
if Param(['cd']):
    # Unfinished
    dir = GetPathInput()
    print(dir)
    if OS == 'Windows':
        os.system('cd /d '+dir)
    else:
        os.system('cd '+dir)

# List Directory Contents
if Param(['dir']):
    #Unfinished
    if OS == 'Windows':
        os.system("echo Current Directory: %cd%")
        print('------------------')
        os.system('dir')
    else:
        os.system('echo Current Directory: ')
        print('------------------')
        os.system('ls')

# To add: write to file, create file, edit file

# --------------------------------------------------------------------------------------
if not params[0] in all_commands:
    restart(['help'])
else: restart()

import subprocess, sys, os, time

version = 1.1

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
        print('\n---------------------------------------------------------------\nUniversal Terminal (v'+str(version)+')\n\nhttps://github.com/MineFartS/Universal-Terminal/\n---------------------------------------------------------------\n')

# Ask for parameters input if none passed through OS's CL
if len(params) == 0:
    params = input(' Console > ').split(' ')
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
    # Reminder to make this work with Unix
    if OS == 'Windows':
        subprocess.Popen('cmd /c ' + command)

# Pause session
def Pause():
    if OS == "Windows":
        os.system("pause")
    else:
        os.system("read -n 1 -s -p 'Press any key to continue . . . '")

# Get next parameter from parameter
def NextParam(parameter):
    return params[params.index(parameter)+1]

# Clears the terminal window
if Param(['cls','clear'],0):
    os.system('cls' if os.name == 'nt' else 'clear')

# Exit with certain parameters
if Param(['exit','quit','leave','end','close','exit()','return'],0):

    Allow_Restart = False

# Show help options if run with 'help' parameter
if Param(['help','/?','-h','-help','?','Help'],0):
    print("** Help Message Goes Here **")

# Run command in OS's terminal
if Param(['os','terminal'],0):
    terminal(ParamText(1,999))

# echo
if Param(['echo','say'],0):
    print(ParamText(1,999))

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
    file = ParamText(1,999).split('"')[1].replace('\\\\','\\')
    for line in open(file,'r+').read().splitlines():
        args = [sys.executable, sys.argv[0],'--hidden-exec']
        for part in line.replace('\n','').split(' '):
            args.append(part)
        subprocess.call(args)
        if '-pause' in params:
            Pause()

# Delete file or folder
if Param(['del','rm','delete','remove','clear','wipe'],0):
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

# --------------------------------------------------------------------------------------
if not params[0] in all_commands:
    restart(['help'])
else: restart()
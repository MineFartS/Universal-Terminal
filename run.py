# The Universal Terminal
# Created By: Phil H.
# Github: https://github.com/MineFartS/Universal-Terminal/

version = 'Beta 1.13'

#=======================================================#
#                 Initial Execution                     #
#=======================================================#

# Import repos & install any missing
try:
    import subprocess, sys, os, time, requests, keyring
except:
    import subprocess,sys,os
    subprocess.call([sys.executable,'-m','pip','install','keyring','requests'])
    subprocess.run([sys.executable, sys.argv[0]])
    exit()

# OS type [Windows|Unix]
OS = {True:'Windows',False:'Unix'}[os.name == 'nt']

# OS Slash Type [\|/]
Slash = {'Windows':'\\','Unix':'/'}[OS]

# [log] - Print text and save as output
def log(value):
    print(value)
    output = keyring.get_password('sys','output')
    if output != '':
        value = '\n' + str(value)
    keyring.set_password('sys','output',keyring.get_password('sys','output')+str(value))

# [dash] - Print dashes to a % of the terminal window 
def dash(percent=100,pad=False):
    dash = int(os.get_terminal_size().columns * percent/100) * '-'
    if pad: log('\n'+dash+'\n')
    else: log(dash)

# Clear window and Print script title if initial start
if len(sys.argv) == 1:
    os.system({False:'clear',True:'cls'}[os.name == 'nt'])
    dash()
    print("\nThe Universal Terminal ("+str(version)+")\n")
    dash()

# Performs various tasks and checks with the passed params
def check(cmd, args, params, help_mess=''):
    # Print first param if 'help --list-cmds' is run
    if cmd == 'help' and '--list-cmds' in args:
        log(params[0])
        return False
    # Run the following if one of Params equals cmd
    if cmd in params:
        # Print all params if '--alt' flag used
        if '--alt' in args:
            for param in params:
                log(param)
            return False
        # Print help message if '--help' flag used
        if '--help' in args:
            log(help_mess)
            return False
        return True
    return False

#=======================================================#
#                  Terminal Commands                    #
#=======================================================#
def main(Input):
    keyring.set_password('sys','output','')
    
    # Replace any variables in input with their actual value
    if '%' in Input:
        for var in Input.split('%'):
            try:
                Input = Input.replace('%'+var+'%',keyring.get_password("user",var))
            except: ''
    cmd, args = Input.split(' ')[0], Input[Input.find(' ')+1:]

    # [about] - Displays details about this script
    params = ['about','ver','info']
    help_mess = 'Shows information about Universal Terminal'
    if check(cmd,args,params,help_mess):    
        dash(40)
        log('The Universal Terminal')
        log('Created by Phil H.')
        dash(40)
        log('Version: '+str(version))
        dash(20)
        log('Github: "https://github.com/minefarts/universal-terminal"')
        dash(40)

    # [Clear] - Clears the terminal window
    params = ['cls','clear']
    help_mess = 'Clear the terminal window'
    if check(cmd,args,params,help_mess):
        os.system({False:'clear',True:'cls'}[os.name == 'nt'])

    # [Exit] - Exit Terminal
    params = ['exit','quit','leave','end','close','return','throw']
    help_mess = 'Exit Universal Terminal'
    if check(cmd,args,params,help_mess):
        keyring.set_password('sys','x','1')

    # [update] - Updates the script from GitHub
    params = ['update']
    help_mess = 'Update to the latest universal terminal version from github'
    if check(cmd,args,params,help_mess):
        log('Fetching latest version from github ... ')
        code = requests.get('https://raw.githubusercontent.com/MineFartS/Universal-Terminal/refs/heads/main/run.py').text
        log('Applying Update ... ')
        cwd = os.getcwd()
        os.chdir(sys.path[0])
        open(sys.argv[0],'w').write(code)
        log('Update Complete')
        os.chdir(cwd)
        main('pause')
        subprocess.run([sys.executable, sys.argv[0]])
        keyring.set_password('sys','x','1')

    # [run] - Runs commands with the computer's default terminal
    params = ['run','os','terminal','term','cmd','bash']
    help_mess = 'Send command to built-in terminal\nos [run command]'
    if check(cmd,args,params,help_mess):
        os.system(args)

    # [echo] - Echoes text back
    params = ['echo','say','repeat','write','text','print']
    help_mess = "'echo [text|var]' or echo [text|%var%]>[filepath]"
    if check(cmd,args,params,help_mess):
        if '>' in args:
            text, file = args.split('>')
            open(file,'a').write('\n'+text)
        else:
            log(args)

    # [wait] - Waits for a certain number of seconds
    params = ['wait','timeout','sleep','hold']
    help_mess = 'Wait for a # of seconds\nwait [seconds]'
    if check(cmd,args,params,help_mess): 
        t = 1
        log('Waiting ...')
        while t < int(args)+1:
            log(t)
            time.sleep(1)
            t += 1

    # [call] - Runs List of commands from text file
    params = ['call','script','execute']
    help_mess = 'Run script file (.txt)\ncall [file]'
    if check(cmd,args,params,help_mess):
        for line in open(args,'r+').read().splitlines():
            main(line)

    # [del] - Delete file or directory
    params = ['del','rm','delete','remove']
    help_mess = 'Delete file or directory\ndel [folder|file]'
    if check(cmd,args,params,help_mess):
        try:
            os.remove(args)
        except:
            os.removedirs(args)

    # [pause] - Pauses session
    params = ['pause','stop','halt','freeze']
    help_mess = 'Pause and wait for key press'
    if check(cmd,args,params,help_mess):
        if OS == "Windows":
            os.system("pause")
        else:
            os.system("read -n 1 -s -p 'Press any key to continue . . . '")

    # [python] - Runs Python
    params = ['python','py3','py','python3']
    help_mess = 'Exceute python\npython [built-in python command]'
    if check(cmd,args,params,help_mess):
        subp = [sys.executable]
        for arg in args.split(' '):
            subp.append(arg)
        subprocess.run(subp)

    # [pip] - Runs Pip
    params = ['pip','pip3']
    help_mess = 'Exceute pip\npip [built-in pip command]'
    if check(cmd,args,params,help_mess):
        subp = [sys.executable,'-m','pip']
        for arg in args.split(' '):
            subp.append(arg)
        subprocess.run(subp)

    # [ping] - ping command
    params = ['ping']
    help_mess = 'Ping an ip address\nping [# of pings] [ip address]'
    if check(cmd,args,params,help_mess):
        if len(args.split(' ')) == 1:
            c, ip = '4', args
        else:
            c, ip = args.split(' ')
        if OS=='Windows':
            os.system('ping -n '+c+' '+ip)
        else:
            os.system('ping -c '+c+' '+ip)

    # [wget] - download web page/file to disk
    params = ['wget','download','get','web','request','save']
    help_mess = 'Save web content as a local file\nwget https://google.com Google.html'
    if check(cmd,args,params,help_mess):
        website, path = args.split(' ')
        open(path,'wb').write(requests.get(website).content)

    # [cd] - Change Directory
    params = ['cd']
    help_mess = 'Change Directory\ncd [directory]'
    if check(cmd,args,params,help_mess):
        os.chdir(args.replace({'\\':'/','/':'\\'}[Slash],Slash))

    # [list] - List Directory Contents
    params = ['list','dir','ls']
    help_mess = 'List directory contents'
    if check(cmd,args,params,help_mess):
        log('')
        items = []
        for path in os.listdir(os.getcwd()):
            if os.path.isdir(path):
                items.append('1[ Folder ] '+path)
            if os.path.isfile(path):
                items.append('2[  File  ] '+path)
        items.sort()
        for item in items:
            log(item[1:])

    # [mkdir] - Make Directory
    params = ['mkdir','mk']
    help_mess = 'Make directory\nmkdir [name]'
    if check(cmd,args,params,help_mess):
        os.makedirs(os.getcwd()+Slash+args+Slash)

    # [var] - Set User Variable
    params = ['var','const','set','let']
    help_mess = 'Set variable\nvar hw=hello world\necho %hw%'
    if check(cmd,args,params,help_mess):
        var, val = args[:args.find('=')], args[args.find('=')+1:]
        keyring.set_password("user",var.strip(),val)
        log('Set %'+var+'% to "'+val+'"')

    # [prompt] - Ask for input
    params = ['prompt','input','ask']
    help_mess = 'Ask for input and save response as variable\nprompt [var]=[Text To Display]'
    if check(cmd,args,params,help_mess):
        var, prompt = args[:args.find('=')], args[args.find('=')+1:]
        keyring.set_password("user",var.strip(),input(prompt))
    
    # [calc] - Caculate math exquations
    params = ['calc','math']
    help_mess = 'Calculate equations\ncalc [var]=[equation]'
    if check(cmd,args,params,help_mess):
        if '=' in args: var, eq = args.split('=')
        else: eq, var = args, False

        if '+' in eq:
            a, b = eq.split('+')
            c = float(a) + float(b)
        if '-' in eq:
            a, b = eq.split('-')
            c = float(a) - float(b)
        if '/' in eq:
            a, b = eq.split('/')
            c = float(a) / float(b)
        if '*' in eq:
            a, b = eq.split('*')
            c = float(a) * float(b)
        if var == False: log(c)
        else:
            log('Set "'+var.strip()+'" to "'+str(c)+'"')
            keyring.set_password("user",var.strip(),str(c))

    # [out] - Save command output as variable
    params = ['out','output']
    help_mess = 'Save command output as variable\nout [var]=[command]'
    if check(cmd,args,params,help_mess):
        var, run = args[:args.find('=')], args[args.find('=')+1:]
        keyring.set_password('user',var,main(run))
        log('Saved output as "%'+var+'%"')
    
    params = ['move','mv']
    help_mess = ''
    #if check(cmd,args,params,help_mess):


    params = ['rn','rename']
    help_mess = ''
#    if check(cmd,args,params,help_mess):

    # To Do:
    # open in text file editor, copy, find,
    # var modification %hi:~1,1% / %hi:~/=\%,
    # for x in y, if, mklink, time

#======================================================================
    # [help] - Display Help Message
    params = ['help','/?','-h','-help','?','h','-?']
    help_mess = 'Show help message'
    if check(cmd,args,params,help_mess):
        if len(Input.split(' ')) == 1:
            # Print help information if there if are no args passed
            dash(15,True)
            main('help --list-cmds')
            dash(15,True)
            log('Try Running "help [command]" for more detailed information')
            log('Note: While in beta, some commands might not have detailed help options')
            dash(15,True)
        else:
            # Show help page for command passed
            log('')
            main(args+' --help')
            log('\nAliases:')
            main(args+' --alt')
    return keyring.get_password('sys','output')
#=======================================================#
#             Input Handling & Execution                #
#=======================================================#

x = 0
keyring.set_password('sys','x',str(x))
while x < 1:
    if len(sys.argv) > 1:
        # If CL arguements are passed, run once with those as input
        text = ''
        for p in sys.argv[1:]:
            text += p + ' '
        text = text[:-1]
        x = 1
    else:
        # If no CL args passed, ask for input on loop
        text = input('\n'+os.getcwd()+' > ')
    # Split the current input by '&&' if '&&' found
    for i in text.split(' && '):
        try:
            # Send input to terminal commands section
            main(i)
        except:
            # Show error message if execution fails
            log('')
            dash(50)
            log('Error: Invalid Syntax or Command')
            log('Run "help" for a list of Commands')
            dash(25)
            log('Please share any glitches or bugs on github')
            log('https://github.com/MineFartS/Universal-Terminal/')
            dash(50)
    x = int(keyring.get_password('sys','x'))
os.system({False:'clear',True:'cls'}[os.name == 'nt'])

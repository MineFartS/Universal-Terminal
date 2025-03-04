# The Universal Terminal
# Created By: Phil H.
# Github: https://github.com/MineFartS/Universal-Terminal/

version = 'Beta 1.12'

last_updated = '2025-02-28'

#=======================================================#
#                   Startup Tasks                       #
#=======================================================#

try:
    import subprocess, sys, os, time, requests, keyring
except:
    import subprocess,sys,os
    subprocess.call([sys.executable,'-m','pip','install','keyring'])

# [dash] - Print dashes to a % of the terminal window 
def dash(percent=100,pad=False):
    dash = int(os.get_terminal_size().columns * percent/100) * '-'
    if pad: print('\n'+dash+'\n')
    else: print(dash)

# clear window and Print script title if initial start
if len(sys.argv) == 1:
    os.system({False:'clear',True:'cls'}[os.name == 'nt'])
    dash()
    print("\nThe Universal Terminal ("+str(version)+")\n")
    dash()

def check(cmd, args, params, help_mess=''):
    if cmd == 'help' and '--list-cmds' in args:
        print(params[0])
        return False
    if cmd in params:
        if '--alt' in args:
            for param in params:
                print(param)
            return False
        if '--help' in args:
            print(help_mess)
            return False
        return True
    return False
    
#=======================================================#
#                  Global Variables                     #
#=======================================================#

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
    cmd, args = Input.split(' ')[0], Input[Input.find(' ')+1:]

    # [about] - Displays details about this script
    params = ['about','ver','info']
    help_mess = 'Shows information about Universal Terminal'
    if check(cmd,args,params,help_mess):    
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

    # [Clear] - Clears the terminal window
    params = ['cls','clear']
    help_mess = 'Clear the terminal window'
    if check(cmd,args,params,help_mess):
        os.system({False:'clear',True:'cls'}[os.name == 'nt'])

    # [Exit] - Exit Terminal
    params = ['exit','quit','leave','end','close','return','throw']
    help_mess = 'Exit Universal Terminal'
    if check(cmd,args,params,help_mess):
        exit()

    # [update] - Updates the script from GitHub
    params = ['update']
    help_mess = 'Update to the latest universal terminal version from github'
    if check(cmd,args,params,help_mess):
        print('Fetching latest version from github ... ')
        code = requests.get('https://raw.githubusercontent.com/MineFartS/Universal-Terminal/refs/heads/main/run.py').text
        print('Applying Update ... ')
        cwd = os.getcwd()
        os.chdir(sys.path[0])
        open(sys.argv[0],'w').write(code)
        print('Update Complete')
        os.chdir(cwd)
        main('pause')
        subprocess.run([sys.executable, sys.argv[0]])
        exit()

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
            print(args)

    # [wait] - Waits for a certain number of seconds
    params = ['wait','timeout','sleep','hold']
    help_mess = 'Wait for a # of seconds\nwait [seconds]'
    if check(cmd,args,params,help_mess): 
        'wait [seconds]\nwait'
        t = 1
        print('Waiting ...')
        while t < int(args)+1:
            print(t)
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

    # [mkdir] - Make Directory
    params = ['mkdir','mk']
    help_mess = 'Make directory\nmkdir [name]'
    if check(cmd,args,params,help_mess):
        os.makedirs(os.getcwd()+Slash+args+Slash)

    # [var] - Set User Variable
    params = ['var','const','set','let']
    help_mess = 'Set variable\nvar hw=hello world\n echo %hw%'
    if check(cmd,args,params,help_mess):
        var, val = args[:args.find('=')], args[args.find('=')+1:]
        keyring.set_password("user_variables",var.strip(),val)
        print('Set %'+var+'% to "'+val+'"')

    # [prompt] - Ask for input
    params = ['prompt','input','ask']
    help_mess = 'Ask for input and save response as variable\nprompt [var]=[Text To Display]'
    if check(cmd,args,params,help_mess):
        var, prompt = args[:args.find('=')], args[args.find('=')+1:]
        keyring.set_password("user_variables",var.strip(),input(prompt))

#======================================================================

    # [help] - Display Help Message
    params = ['help','/?','-h','-help','?','h','-?']
    help_mess = 'Show help message'
    if check(cmd,args,params,help_mess):
        if len(Input.split(' ')) == 1:
            dash(15,True)
            main('help --list-cmds')
            dash(15,True)
            print('Try Running "help [command]" for more detailed information')
            print('Note: While in beta, some commands might not have detailed help options')
            dash(15,True)
        else:
            print('\nHelp for "'+args+'":')
            main(args+' --help')
            print('\nDifferent options for "'+args+'":')
            main(args+' --alt')
                

    # To Do:
    # open in text file editor, use cmd output as input

x = 0
while x < 1:
    if len(sys.argv) > 1:
        text = ''
        for p in sys.argv[1:]:
            text += p + ' '
        text = text[:-1]
        x = 1
    else:
        text = input('\n'+os.getcwd()+' > ')

    for i in text.split('&&'):
        try:
            if '%' in i:
                for var in i.split('%'):
                    try:
                        i = i.replace('%'+var+'%',keyring.get_password("user_variables",var))
                    except: ''
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

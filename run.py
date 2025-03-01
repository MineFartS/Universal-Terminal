# The Universal Terminal
# Created By: Phil H.
# Github: https://github.com/MineFartS/Universal-Terminal/

version = 'Beta 1.10'

last_updated = '2025-02-28'

#=======================================================#
#                   Startup Tasks                       #
#=======================================================#

error = False
try:
    try:
        import subprocess, sys, os, time, requests
    except:
        import subprocess,sys,os
        repos = []

        args = [sys.executable,'-m','pip','install']
        for repo in repos:
            args.append(repos)
        subprocess.call(args)
        restart()

    # [restart] - Restarts / Starts a new line
    Allow_Restart = True
    def restart(parameters=[]):
        if Allow_Restart:
            args = [sys.executable, sys.argv[0], '--restart']
            for p in parameters: args.append(p)
            subprocess.call(args)
            exit()
        else:
            exit()

    # [dash] - Print dashes to a % of the terminal window 
    def dash(percent=100,pad=False):
        x = 0
        dash = ''
        while x < os.get_terminal_size().columns*[percent/100][0]:
            dash += '-'
            x += 1
        if pad: print('\n'+dash+'\n')
        else: print(dash)
        return dash

    # Get CL parameters 
    params = sys.argv[1:999]

    # Remove any system arguements (arguements only used by the script itelf for subprocess, etc.) from 'params' and append them to 'arguements' insted
    arguements = []
    for arg in ['--restart','--hidden-exec','--display-help-message','--list-phrases']:
        if arg in params: 
            params.remove(arg)
            arguements.append(arg)

    # Print script title if initial start
    if not '--restart' in arguements and not '--hidden-exec' in arguements:
        os.system('cls' if os.name == 'nt' else 'clear')
        dash()
        print("\nThe Universal Terminal ("+str(version)+")\n")
        dash()
        
    # Ask for input if no CL parameters passed
    if len(params) == 0:
        params = input('\n'+os.getcwd()+' > ').split(' ')

    # Exit after the current execution if CL parameters passed
    else:
        if not '--restart' in params: Allow_Restart = False

    #=======================================================#
    #                   Global Variables                    #
    #=======================================================#

    all_commands = []
    help_commands = []

    # OS type (Windows, Unix)
    OS = {True:'Windows',False:'Unix'}[os.name == 'nt']

    # OS Slash Type (\, /)
    Slash = {'Windows':'\\','Unix':'/'}[OS]

    # Path with current script file
    ScriptPath = sys.path[0] + Slash + sys.argv[0]

    #=======================================================#
    #                       Functions                       #
    #=======================================================#

    # [ListifyArray] - Formats an array as a plain text list separated by lines
    def ListifyArray(array):
        return str(array)[1:-1].replace("'",'').replace(', ','\n')

    # [Param] - Checks if certain parameter is one of many values
    def Param(names,index=0):
        if '--list-phrases' in arguements and params[0] in names:
            print('\nAlternatives to "'+params[0]+'":\n'+ListifyArray(names))
            restart()
        help_commands.append(names[0])
        for name in names:
            all_commands.append(name)
            if name.capitalize() == params[index].capitalize(): return True
        return False

    # [ParamText] - Gets a range of parameters as plain text
    def ParamText(min=1,max=999):
        return str(params[min:max]).replace('[','').replace(']','').replace("'",'').replace(',','')

    # [Flag] - Gets details about a flag in params
    def Flag(flag):
        if not flag in params:
            return [False,'']
        else:
            return [True, params[params.index(flag)+1]]

    # [terminal] - Run command in the OS's build in terminal
    def terminal(command):
        os.system(command)

    # [Pause] - Pause session
    def Pause():
        if OS == "Windows":
            os.system("pause")
        else:
            os.system("read -n 1 -s -p 'Press any key to continue . . . '")

    # [NextParam] - Find the value of a parameter by giving the value of the one before it
    def NextParam(parameter):
        return params[params.index(parameter)+1]

    # [GetPathInput] - Get Parameters with spaces (like paths)
    def GetPathInput(start=1):
        try:
            return ParamText(start,999).split('"')[1]
        except:
            return ParamText(1,999)

    # [help] - Prints advanced help messages for functions
    def help(message=''):
        if '--display-help-message' in sys.argv:
            print(message)
            restart()

    # [clear] - clear the terminal window
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    # [command] - run a command from this terminal as a sub process
    def command(parameters=[]):
        args = [sys.executable, sys.argv[0],'--hidden-exec']
        for p in parameters:
            args.append(str(p))
        subprocess.call(args)

    #=======================================================#
    #                  Terminal Commands                    #
    #=======================================================#

    # Divides Input into multiple commands by '&&'
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
    if Param(['about','ver','info']):
        help('')
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
    if Param(['cls','clear']):
        help('')
        clear()

    # [Exit] - Exit Terminal
    if Param(['exit','quit','leave','end','close','return','throw']):
        help('')
        Allow_Restart = False

    # [update] - Updates the script form GitHub
    if Param(['update']):
        help('')
        print('Fetching latest version from github ... ')
        code = requests.get('https://raw.githubusercontent.com/MineFartS/Universal-Terminal/refs/heads/main/run.py').text
        print('Applying Update ... ')
        cwd = os.getcwd()
        os.chdir(sys.path[0])
        open(sys.argv[0],'w').write(code)
        print('Update Complete')
        os.chdir(cwd)

    # [os] - Runs commands with the computer's default terminal
    if Param(['run','os','terminal','term','cmd','bash']):
        help('')
        terminal(ParamText(1,999))

    # [echo] - Echoes text back
    if Param(['echo','say','repeat','write','text','print']):
        help("'echo [text]' - writes text to the console\n'echo [text]>[file]' - writes text to a file")
        input = ParamText(1,999)
        if '>' in input:
            text, file = input.split('>')
            if '"' in text:
                text = text.split('"')[1]
            open(file,'a').write('\n'+text)
        else:
            print(input)

    # [wait] - Waits for a certain number of seconds
    if Param(['wait','timeout','sleep','hold'],0):
        help('wait [seconds]\nwait')
        if '--hide' in params:
            params.remove('--hide')
            time.sleep(int(params[1]))
        else:
            x = 1
            while x < int(params[1])+1:
                print(x,'of',int(params[1]),'seconds')
                time.sleep(1)
                x += 1

    # [call] - Runs List of commands from text file
    if Param(['call','script','execute']):
        help('')
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
        help('')
        Pause()

    # [python] - Runs Python
    if Param(['python','py3','py','python3']):
        help('')
        args = [sys.executable]
        for p in params[1:]:
            args.append(p)
        subprocess.call(args)

    # [pip] - Runs Pip
    if Param(['pip','pip3']):
        help('')
        args = [sys.executable,'-m','pip']
        for p in params[1:]:
            args.append(p)
        subprocess.call(args)

    # [ping] - ping command
    if Param(['ping']):
        help('')
        if Flag('-n')[0] or Flag('-c')[0]:
            for p in ['-n','-c']:
                if Flag(p)[0]:        
                    c = Flag(p)[1]
                    params.remove(p)
                    params.remove(c)
        else:
            c = '4'
        if OS=='Windows':
            terminal('ping -n '+c+' '+params[1])
        else:
            terminal('ping -c '+c+' '+params[1])

    # [wget] - download web page/file to disk
    if Param(['wget','download','get','web','request','save']):
        help('')
        input = ParamText().split('"')[1:4]
        open(input[2],'wb').write(requests.get(input[0]).content)

    # [cd] - Change Directory
    if Param(['cd']):
        help()
        os.chdir(ParamText())

    # [list] - List Directory Contents
    if Param(['list','dir','ls']):
        help()
        print('')
        for path in os.listdir(os.getcwd()):
            if os.path.isdir(path):
                print('[ Folder ]',path)
            if os.path.isfile(path):
                print('[  File  ]',path)

    if Param(['mkdir']):
        os.makedirs(os.getcwd()+Slash+ParamText()+Slash)

    # To Do: 
    # Fix Params Dual Error Message
    # open in text file editor, use cmd output as input, variables (%var%, etc)

    #=======================================================#
    #                   Help Message                        #
    #=======================================================#

    # [help] - Display Help Message
    if Param(['help','/?','-h','-help','?','h','-?'],0):
        if len(params) == 1: 
            dash(15,True)
            print("Commands:\n")
            help_commands.sort()
            print(ListifyArray(help_commands))
            dash(15,True)
            print('Try Running "help [command]" for more detailed information')
            print('Note: While in beta, some commands might not have help options')
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

    #=======================================================#
    #                   Restart / Error                     #
    #=======================================================#
    if not params[0] in all_commands: error = True
except:
    error = True

if error == True:
    print('')
    dash(50)
    print('Error: Invalid Syntax or Command')
    print('Run "help" for a list of Commands')
    dash(25)
    print('Please share any glitches or bugs on github')
    print('https://github.com/MineFartS/Universal-Terminal/')
    dash(50)
    restart()
restart()

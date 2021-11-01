#  overthewire.org/wargames/bandit/bandit0.html
#  The goal of this level is for you to log into the game using SSH.
#  The host to which you need to connect is bandit.labs.overthewire.org, on port 2220.
#  The username is bandit0 and the password is bandit0.
#  Once logged in, go to the Level 1 page to find out how to beat Level 1.
import paramiko

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('[*] Output')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    import getpass
    user = input('Username: ') or 'bandit0'
    password = getpass.getpass()

    ip = input('Enter server IP: ') or 'bandit.labs.overthewire.org'
    port = input('Enter port or <CR>: ') or 2220
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)
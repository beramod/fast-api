import paramiko

class ShellScript:
    userName = 'soulinno'
    password = 'soulinno11!!'
    result = ''
    ip = ''
    port = 0
    ssh = paramiko.SSHClient()

    def __init__(self, ip, port):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ip = ip
        self.port = port

    def connect(self):
        self.ssh.connect(self.ip, username=self.userName, password=self.password, port=self.port)

    @classmethod
    def command(cls, command):
        stdin, stdout, stderr = cls.ssh.exec_command(command)
        cls.result = stdout.read()
        cls.ssh.close()

    @classmethod
    def getResult(cls):
        return str(cls.result)[2:].replace("\\n", "").replace("'", "")

    @classmethod
    def getProcessCnt(cls, target):
        command = "pgrep -lf " + target + " | wc -l"
        stdin, stdout, stderr = cls.ssh.exec_command(command)
        cls.result = stdout.read()
        cls.ssh.close()
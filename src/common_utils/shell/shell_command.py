import paramiko

class ShellCommand:
    def __init__(self, ip, port, user_name, password):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ip = ip
        self.port = port
        self.user_name = user_name
        self.password = password
        self.result = None

    def connect(self):
        if self.password is not None:
            self.ssh.connect(self.ip, username=self.user_name, password=self.password, port=self.port)
        else:
            self.ssh.connect(self.ip, username=self.user_name, port=self.port)

    def command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        self.result = stdout.readlines()
        self.ssh.close()

    def get_result(cls):
        return str(cls.result)[2:].replace("\\n", "").replace("'", "")

    def get_process_cnt(self, target):
        command = "pgrep -lf " + target + " | wc -l"
        stdin, stdout, stderr = self.ssh.exec_command(command)
        self.result = stdout.read()
        self.ssh.close()
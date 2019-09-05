from docker_build.src.API_Docker import API_Docker


class Ubuntu_Build:

    # helpers
    def __init__(self):
        self.build_name = 'ubuntu-with-policy'
        self.docker     = API_Docker()

    def bash(self,bash_cmd):
        result = self.run(['bash', '-c', bash_cmd])
        if result.get('ok'):
            lines = result.get('console')
            if len(lines) == 1:
                return lines.pop()
            return lines
        return result.get('error')

    def build(self):
        result = self.docker.build(self.build_name)
        if result.get('ok') is True and 'Successfully tagged ubuntu-with-policy:latest' in result.get('console'):
            return True
        return False

    def run(self, params=None):
        return self.docker.run(self.build_name, params)

    def file_contents(self,path):
        params = ['cat', path]
        return '\n'.join(self.run(params).get('console'))

    # linux commands

    def file_etc_common_password(self):
            return self.file_contents('/etc/pam.d/common-password')

    def file_etc_motd(self):
        return self.file_contents('/etc/motd')

    def file_etc_passwd(self):
        return self.file_contents('/etc/passwd')

    def file_etc_shadow(self):
        return self.file_contents('/etc/shadow')





    def uname(self):
        return self.run(['uname', '-a']).get('console').pop()
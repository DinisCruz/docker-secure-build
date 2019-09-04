from docker_build.src.API_Docker import API_Docker


class Ubuntu_Build:

    def __init__(self):
        self.build_name = 'ubuntu-with-policy'
        self.docker     = API_Docker()

    def build(self):
        result = self.docker.build(self.build_name)
        if result.get('ok') is True and 'Successfully tagged ubuntu-with-policy:latest' in result.get('console'):
            return True
        return False

    def run(self, params=None):
        return self.docker.run(self.build_name, params)
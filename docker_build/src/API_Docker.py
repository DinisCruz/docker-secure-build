from pbx_gs_python_utils.utils.Files import Files
from pbx_gs_python_utils.utils.Process import Process


class API_Docker:

    def __init__(self):
        self.images_path = Files.path_combine(__file__,'../../../docker')

    def build(self, build_name):

        build_path = Files.path_combine(self.images_path, build_name)
        params = ['build', '-t', build_name, build_path]
        return  self.docker_exec(params)

    def docker_exec(self, params=None, cwd=None):
        if params is None: params = []
        executable = 'docker'
        result = Process.run(executable, params,cwd)
        if result.get('stderr') != '':
            return { 'ok': False, 'console': result.get('stdout').strip().split('\n'), 'error'  : result.get('stderr').split('\n') }
        return     { 'ok': True , 'console': result.get('stdout').strip().split('\n')}

    def run(self, image_name, cmd=None):
        params = ['run',image_name]
        if type(cmd) == str : params.append(cmd)
        if type(cmd) == list: params.extend(cmd)
        return self.docker_exec(params)

from unittest import TestCase

from pbx_gs_python_utils.utils.Dev import Dev
from pbx_gs_python_utils.utils.Files import Files

from docker_build.src.API_Docker import API_Docker


class test_API_Docker(TestCase):

    def setUp(self):
        self.api    = API_Docker()
        self.result = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def test_ctor(self):
        assert type(self.api).__name__ == 'API_Docker'
        assert Files.folder_exists(self.api.images_path)


    def test_build(self):
        assert 'Successfully tagged alpine-python:latest' in self.api.build('alpine-python').get('console')
        result = self.api.run('alpine-python', ['python3', '--version'])
        assert result.get('ok') is True
        assert result.get('console') == ['Python 3.7.3']

    def test_exec(self):
        assert self.api.exec().get('error')[1] ==  'Usage:\tdocker [OPTIONS] COMMAND'

    def test_run(self):
        assert 'Hello from Docker!' in self.api.run('hello-world').get('console')

    def test_run__with_params(self):
        assert 'bin' in self.api.run('ubuntu', 'ls').get('console')


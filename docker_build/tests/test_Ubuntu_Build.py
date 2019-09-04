from unittest import TestCase

from pbx_gs_python_utils.utils.Dev        import Dev
from docker_build.src.builds.Ubuntu_Build import Ubuntu_Build


class test_Ubuntu_Build(TestCase):

    def setUp(self):
        self.ubuntu_build = Ubuntu_Build()
        self.result       = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def test_build(self):
        self.result = self.ubuntu_build.build()

    def test_run(self):
        self.result = self.ubuntu_build.run()

    def test_run_with_params(self):
        self.result = self.ubuntu_build.run(['uname', '-a'])
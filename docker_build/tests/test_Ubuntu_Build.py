from unittest import TestCase

from pbx_gs_python_utils.utils.Dev        import Dev
from docker_build.src.builds.Ubuntu_Build import Ubuntu_Build


class test_Ubuntu_Build(TestCase):

    def setUp(self):
        self.ubuntu = Ubuntu_Build()
        self.result       = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def test_bash(self):
        self.ubuntu.bash('echo some text> abc.txt; cat abc.txt') == 'some text'

    def test_build(self):
        self.result = self.ubuntu.build()

    def test_file_contents(self):
        assert 'password-related modules common' in self.ubuntu.file_contents('/etc/pam.d/common-password')

    def test_run(self):
        self.result = self.ubuntu.run()

    def test_run_with_params(self):
        self.result = self.ubuntu.run(['uname', '-a'])


    # linux commands
    def test_file_etc_common_password(self):
        assert 'password-related modules common to all ' in self.ubuntu.file_etc_common_password()

    def test_file_etc_passwd(self):
        assert 'root:x:0:0:root:/root:/bin/bash' in  self.ubuntu.file_etc_passwd()

    def test_file_etc_passwd(self):
        assert 'root:*:18115:0:99999:7:::\n' in  self.ubuntu.file_etc_shadow()

    def test_uname(self):
        assert '4.9.125-linuxkit' in self.ubuntu.uname()
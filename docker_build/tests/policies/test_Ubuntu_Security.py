from unittest import TestCase

from pbx_gs_python_utils.utils.Dev import Dev

from docker_build.src.builds.Ubuntu_Build import Ubuntu_Build


class test_Ubuntu_Security(TestCase):

    def setUp(self):
        self.ubuntu = Ubuntu_Build()
        self.result = None


    def tearDown(self):                 # to help unit test developmennt
        if self.result is not None:
            Dev.pprint(self.result)

    def test_POLICY_5__required_passwords_to_be_16_chars(self):
        # confirm that the password settings exists in the '/etc/pam.d/common-password' file
        assert 'pam_cracklib.so try_first_pass retry=3 minlen=16' in self.ubuntu.file_etc_common_password()

        # create a user with a weak/short password and it should fail
        assert 'BAD PASSWORD: is too simple' in self.ubuntu.bash('useradd aaa; echo aaa:!!@@__           | chpasswd')

        # create a user with a strong password (which should work ok)
        assert ''                            == self.ubuntu.bash('useradd aaa; echo aaa:!!@@__aa__bb__cc | chpasswd')


    def test_POLICY_9__show_message_on_login(self):
        assert "This system is for the use of authorised" in self.ubuntu.file_etc_motd()


    def test_POLICY_22_anti_virus_is_installed(self):
        assert '----------- SCAN SUMMARY -----------' in self.ubuntu.run(['clamscan','–-help']).get('console')

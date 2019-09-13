FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y libpam-cracklib

# 3.1.2.1 - Require all passwords/passphrases to be at least 16 characters in length                  - https://ubuntu-policy.atlassian.net/browse/POLICY-5
# 3.1.2.2 - Require complex passwords, consisting of both numeric, alphabetic and special characters  - https://ubuntu-policy.atlassian.net/browse/POLICY-5
RUN echo 'password required pam_cracklib.so try_first_pass retry=3 minlen=16 lcredit=1 ucredit=1 dcredit=2 ocredit=1 difok=2 reject_username' >> /etc/pam.d/common-password

# 3.2.1 System Administrator Responsibilities (login message)                                         - https://ubuntu-policy.atlassian.net/browse/POLICY-9

RUN echo "This system is for the use of authorised users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel. In the course of monitoring individuals improperly using this system, or in the course of system maintenance, the activities of authorised users may also be monitored.\n" > /etc/motd
RUN echo "Anyone using this system expressly consents to such monitoring and is advised that if such monitoring reveals possible criminal activity, system personnel may provide the evidence of such monitoring to law enforcement" >> /etc/motd

# 7.1 Software Configuration (ClamAV installed)                                                       - https://ubuntu-policy.atlassian.net/browse/POLICY-22
RUN apt-get -y install clamav


CMD echo 'all done'
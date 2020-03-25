#!/usr/bin/env bash
# connect with puppet
file_line { 'Declare_identity_file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Turn_off_passwd_auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
}

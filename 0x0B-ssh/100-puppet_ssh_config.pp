# modifies the ssh configurayion file
file {'/home/ubuntu/.ssh/config':
  ensure  => present,
  path    => '/home/ubuntu/.ssh/config',
  content => 'Host 54.160.84.211
                IdentityFile /home/ubuntu/.ssh/school
                PasswordAuthentication no'
}

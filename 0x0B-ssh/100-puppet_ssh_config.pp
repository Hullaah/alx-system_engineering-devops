# modifies the ssh configurayion file
file {'/home/ubuntu/.ssh/config':
  ensure  => present,
  path    => '/home/hullaah/.ssh/config',
  content => 'Host 54.160.84.211
                IdentityFile ~/.ssh/school
                PasswordAuthentication no'
}

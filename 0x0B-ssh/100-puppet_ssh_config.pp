# modifies the ssh configurayion file
file {'/home/hullaah/.ssh/config':
  ensure  => present,
  path    => '/home/hullaah/.ssh/config',
  content => "Host 54.160.84.211\n\tIdentityFile /home/ubuntu/.ssh/school\n\tPasswordAuthentication no"
}

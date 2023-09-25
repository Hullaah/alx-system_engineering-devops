# modifies the ssh configurayion file
file {'/etc/ssh/ssh_config':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => "Host 54.160.84.211\n\tIdentityFile /home/ubuntu/.ssh/school\n\tPasswordAuthentication no"
}

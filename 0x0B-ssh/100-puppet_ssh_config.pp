# modifies the ssh configurayion file
file {'/home/ubuntu/.ssh/config':
  ensure  => present,
  path    => /home/ubuntu/.ssh/config
  content => "Host 54.160.84.211\n\tIdentityFile /home/ubuntu/.ssh/school\n\tPasswordAuthentication no"
}

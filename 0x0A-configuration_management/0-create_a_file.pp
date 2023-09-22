# creates a file, school, in /tmp with permisiion 0744, owner www-data, group www-data and content 'I love Puppet'.
file { '/tmp/school':
    ensure  => present,
    path    => '/tmp/school',
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data'
}

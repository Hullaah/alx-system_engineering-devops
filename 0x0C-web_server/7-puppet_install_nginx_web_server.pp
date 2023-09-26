# installs and configures an nginx server
package { 'nginx':
    ensure => installed,
}

file {'/var/www/html/index.html':
    content => 'Hello World!',
}

service {'nginx':
    ensure => running,
    require => Package['nginx']
}

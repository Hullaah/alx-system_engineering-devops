# installs and configures an nginx server
exec { 'update':
  command => 'apt-get update -y',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page",
}

exec { 'redirect_me':
  command => ['sed', '-i', 's`server_name _;`server_name _;\n\tlocation /redirect_me {return 301 https://github.com/Hullaah;}`', '/etc/nginx/sites-available/default'],
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}

exec { '404_error':
  command => ['sed', '-i', 's`root /var/www/html;`root /var/www/html;\n\terror_page 404 /404.html;`', '/etc/nginx/sites-available/default'],
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

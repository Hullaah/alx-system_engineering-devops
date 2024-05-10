# installs flask from pip3
package { 'pip3':
  ensure => installed,
  name   => 'python3-pip',
}

package { 'flask':
  ensure   => '2.1.0',
  name     => 'Flask',
  require  => Package['pip3'],
  provider => 'pip3',
}

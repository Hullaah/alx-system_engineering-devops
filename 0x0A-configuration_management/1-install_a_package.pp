class { 'nodejs':
  version => '3.8.10'
}

package {'flask':
  ensure   =>  '2.10',
  provider => 'pip3',
  require  => Class['nodejs'],
}

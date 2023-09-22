# kills the procss killmenow
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}

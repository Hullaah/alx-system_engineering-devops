# kills a process named killmenow
exec { 'killmenow':
  command => 'kill -9 killmenow',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}

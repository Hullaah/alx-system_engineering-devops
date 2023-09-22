exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin', '/usr/local/bin'],
  refreshonly => true,
  subscribe   => Exec['start_killmenow_process'],
  onlyif      => 'pgrep killmenow',
}

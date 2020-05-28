file { 'replace last line':
    ensure  => present,
    path    => '/etc/default/nginx',
    content => 'ULIMIT="-n 4096"',
}

service { 'nginx':
    ensure    => running,
    subscribe => File['/etc/default/nginx']
}
#/etc/default/nginx -- ULIMIT="-n 15" to ULIMIT="-n 4096"

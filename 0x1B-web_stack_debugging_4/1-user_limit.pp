# Change the OS configuration
file { 'destroyer of worlds':
    ensure  => present,
    path    => '/etc/security/limits.conf',
    content => '#This file has been wiped hahaha'
}

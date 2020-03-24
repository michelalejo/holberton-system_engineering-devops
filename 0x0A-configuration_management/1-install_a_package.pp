# Install puppet-lint --version 2.1.1.
package { 'puppet-lint':
  provider   => 'gem',
  ensure => '2.1.1',
}
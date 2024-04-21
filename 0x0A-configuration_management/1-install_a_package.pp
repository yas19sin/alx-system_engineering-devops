# Install the Flask web framework via pip3

package { 'flask':
  ensure   => 'installed',
  version  => '2.1.0',
  provider => 'pip3',
}

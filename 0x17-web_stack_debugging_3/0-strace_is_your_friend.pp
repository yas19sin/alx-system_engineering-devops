# Puppet manifest to fix typo in wp-settings.php causing Apache 500 error

exec { 'wordpress-settings.php fix':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

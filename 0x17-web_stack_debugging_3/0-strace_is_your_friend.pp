# Puppet manifest to fix typo in wp-settings.php causing Apache 500 error
exec { 'fix_wordpress_typo':
  command => 'sed -i "s/\.phpp/\.php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
  onlyif  => 'grep -q "\.phpp" /var/www/html/wp-settings.php',
}

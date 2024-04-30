# Set up an Ubuntu web server with Nginx and custom HTTP header

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => present,
  name    => 'nginx',
  require => File['/var/www/html/index.html'],
}

file { '/var/www/html/index.html':
ensure  => present,
    content => 'Hello World!',
}

file_line { 'add_header':
ensure  => present,
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
    line    => 'add_header X-Served-By $hostname;',
}

file_line { 'redirect_me':
ensure  => present,
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://worldsim.nousresearch.com permanent;',
}

service { 'nginx':
  ensure     => running,
  hasrestart => true,
  require    => [ Package['nginx'], File['/var/www/html/index.html'] ],
}

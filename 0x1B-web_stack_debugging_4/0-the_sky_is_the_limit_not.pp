# Increase Nginx request handling capacity by raising the max open files limit.  

exec { 'Increase Nginx max open files limit':  
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',  
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',  
}

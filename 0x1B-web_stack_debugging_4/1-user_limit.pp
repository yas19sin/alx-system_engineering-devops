# Modify OS security settings to ensure the 'holberton' user can log in  
# and open files without encountering any error messages.  

exec { 'Update OS security configuration':  
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',  
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'  
}

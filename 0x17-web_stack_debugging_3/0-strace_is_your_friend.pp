# Fix apache error 
exec { 'Fix WordPress site':
  command  => 'sudo sed -i.bak \'s/.phpp/.php/\' /var/www/html/wp-settings.php',
  provider => shell,
}


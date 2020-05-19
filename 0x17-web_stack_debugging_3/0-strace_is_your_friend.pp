# With error withh sed to reemplase and remove a extra p.
exec {'fix_with_sed':
    command  => 'sed -i "s|class-wp-locale.phpp|class-wp-locale.php|g" /var/www/html/wp-settings.php',
    provider => shell,
}

include aventurella-apache2
include aventurella-ntp
include aventurella-vim

aventurella-apache2::module {'enable_apache_modules':
    modules => ['rewrite'],
    enable => true,
}

aventurella-apache2::vhost {'ctflorals':
    docroot        => '/var/www/ctflorals',
    server_name    => 'ctflorals.com',
    server_aliases => ['www.ctflorals.com', 'catherinethoeleflorals.com', 'www.catherinethoeleflorals.com'],
    allow_override => true,
}

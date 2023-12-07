# Prepare your web servers using puppet
$apt_update_command = '/usr/bin/env apt-get -y update'
$apt_install_nginx_command = '/usr/bin/env apt-get -y install nginx'
$web_static_directory = '/data/web_static'
$releases_test_directory = "${web_static_directory}/releases/test"
$shared_directory = "${web_static_directory}/shared"
$index_content = 'Holberton School'

exec { 'apt-get-update':
  command => $apt_update_command,
} ->
exec { 'install-nginx':
  command => $apt_install_nginx_command,
} ->
file { [$releases_test_directory, $shared_directory]:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
} ->
file { "${releases_test_directory}/index.html":
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  content => $index_content,
} ->
exec { 'create-symlink':
  command => "/usr/bin/env ln -sf ${releases_test_directory} ${web_static_directory}/current",
} ->
exec { 'configure-nginx':
  command => '/usr/bin/env sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
} ->
exec { 'restart-nginx':
  command => '/usr/bin/env service nginx restart',
} ->
exec { 'change-owner':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}

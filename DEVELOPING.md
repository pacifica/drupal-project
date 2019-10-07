# Developing Pacifica Features

Developing Pacifica features in Drupal 8 uses the composer
configuration in the `8.x-vcs` branch of the
[pacifica/drupal-project](https://github.com/pacifica/drupal-project.git)
repository.

## Development Dependencies

Install the required dependencies first.

 * [Docker](https://docs.docker.com/install/)
 * [PHP 7.x](https://www.php.net/manual/en/install.php)
 * [Drush Launcher](https://github.com/drush-ops/drush-launcher#installation---phar)
 * [Drupal Launcher](https://drupalconsole.com/docs/en/getting/launcher)

NOTE: Make sure local MySQL and web servers are stopped.
Docker will provide those services.

## Setup Testing Environment

The testing environment is driven by composer scripts. The environment
is configured using [Drupal VM](https://github.com/geerlingguy/drupal-vm).

```
composer create-project pacifica/drupal-project:8.x-vcs-dev pacifica-site --no-interaction --keep-vcs
cd pacifica-site
composer install
composer run-script --timeout 3600 setup-testing
```

This should get your Pacifica Drupal site available at
[localhost](http://localhost:8080) and MySQL is available at
[localhost](mysql://drupal:drupal@127.0.0.1:3306/drupal).

## Install and Login to Drupal

Drush is available with a local site alias for development.

```
drush @self.docker si --site-name=Drupal --db-url=mysql://drupal:drupal@127.0.0.1:3306/drupal pacifica
drush @self.docker uli
```

## Destroy Testing Environment

To cleanup the environment and remove all containers.

```
composer run-script nuke-testing
```

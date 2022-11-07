# 🐘 Symfony

[Symfony](https://symfony.com/)

[API Platform](https://api-platform.com/)

[Doctrine](https://www.doctrine-project.org/)

See also:
- [test](test)
- [linter](linter)

## Getting started

**Requirement**

- [PHP >= 8](https://www.php.net/downloads.php)
- [Composer](https://getcomposer.org/)
- [Symfony CLI](https://symfony.com/download)

- Add local `.env.local` file
  ```shell
  APP_DEBUG=0
  DATABASE_URL="sqlite:///%kernel.project_dir%/var/data.sqlite"
  ```

**Install**

```
symfony check:requirements
composer install
```

**Init DB**

```
composer migrate-db-run
```

**Runnning**

```bash
composer start
```

Access to local api <http://localhost:8080/api/>

## Toolings

**Code formating**

```bash
composer format
```

**Code linting**

```bash
composer lint
```

**Testing**

```bash
composer test
```

## Project structure

```
📂symfony
 ┣ 📂bin
 ┣ 📂config
 ┣ 📂migration
 ┣ 📂public
 ┣ 📂src
 ┃ ┣ 📂ApiResource
 ┃ ┣ 📂Controller
 ┃ ┣ 📂Entity
 ┃ ┣ 📂Enum
 ┃ ┣ 📂Repository
 ┃ ┗ 📜Kermel.php
 ┣ 📂templates
 ┣ 📂tests
 ┃ ┣ 📂functional
 ┃ ┗ 📜bootstrap.php
 ┣ 📜.env
 ┣ 📜.env.test
 ┣ 📜.php-cs-fixer.dist.php
 ┣ 📜composer.json
 ┣ 📜composer.lock
 ┣ 📜phpunit.xml.dist
 ┗ 📜symfony.lock
```


| Folder/File | Descripton |
| ----------- | ---------- |

## Sources

- [Building a REST API with Symfony and API platform](https://digitalfortress.tech/tutorial/rest-api-with-symfony-and-api-platform/)
- [Youtube API Platform by Grafikart.fr](https://www.youtube.com/playlist?list=PLjwdMgw5TTLU7DcDwEt39EvPBi9EiJnF4)
- https://github.com/api-platform/core/pull/5120

## How to

### Update project

List outdated dependencies
```
composer outdated
composer update
composer update "symfony/*" --with-all-dependencies
```
See [API Platform - Upgrade Guide](https://api-platform.com/docs/core/upgrade-guide/)

## Create a DB migration

```
composer migrate-db-create
```

## Clear cache

```
rm -rf var/cache
```
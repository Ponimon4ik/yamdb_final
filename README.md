# yamdb_final
API YAMBD - это интерфейс, который собирает отзывы пользователей на произведения

### Используемые технологии:

+ Django,
+ Django rest framework,
+ Simple JWT,
+ Python
+ Docker

### Установка Docker:

Установите Docker
```
sudo apt install docker
```

Установите docker-compose, с этим вам поможет [официальная документация](https://docs.docker.com/compose/install/)

### Как запустить проект:

Клонировать репозиторий и перейти в директорию infra:
```
git clone https://github.com/Ponimon4ik/infra_sp2
```
```
cd infra
```

Cоздать env-файл и прописать переменные окружения в нём:
```
touch .env
```
```
DEBUG_STATUS = FALSE # устанавливаем режим отладки
ALLOWED_HOST = ['*'] # указываем разрешенные хосты (установите свои)
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
SECRET_KEY= secret_key_django # ключ django приложения
```

Запустить docker-compose
```
docker-compose up -d
```

Выполнить по очереди команды:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

### Как загрузить данные:

Скопировать данные в контейнер:
```
docker-compose cp fixtures.json web:/app
```
Выполнить команду:
```
docker-compose exec web python manage.py loaddata fixtures.json
```

### Автор:

+ Стефанюк Богдан

### Ссылка на проект:
[Yamdb_final](http://51.250.4.172:80/admin/)

![Yamdb_workflow](https://github.com/Ponimon4ik/yamdb_final/workflows/Yamdb_workflow/badge.svg)

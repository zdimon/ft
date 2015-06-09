Руководство по установке на платформу Ubuntu 14.

Устанавливем Python.

    sudo apt-get install python-dev

Устанавливаем виртуальное окружение.

    sudo apt-get install python-virtualenv

Создаем виртуальное окружение.

    virtualenv ft_ve

Переходим в окружение и активируем его.

    cd ft_ve
    source ./bin/activate

Клонируем проект из репозитория git.

    git clone git@github.com:zdimon/ft.git

Переходим в каталог проекта и устанавливаем зависимости.

    cd ft
    pip install -r requirements.txt

Создаем базу данных.

    ./manage.py syncdb

Загружаем тестовые данные.

    ./manage.py load_data

Запускаем веб сервер.

    ./manage.py runserver

Проверяем работу программы в браузере.

    http://localhost:8000/admin

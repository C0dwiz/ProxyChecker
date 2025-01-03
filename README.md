# Proxy Checker

Proxy Checker — это программа на Python, которая позволяет проверять работоспособность прокси-серверов, указанных в текстовом файле. Она отправляет HTTP-запросы через каждый прокси и выводит результаты проверки в консоль.

## Установка

1. Убедитесь, что у вас установлен Python 3.x. Вы можете скачать его с [официального сайта Python](https://www.python.org/downloads/).

2. Клонируйте этот репозиторий или скачайте файлы проекта на свой компьютер.

3. Установите необходимые зависимости. Для этого выполните следующую команду в терминале:

```shell
pip install -r requirements.txt
```

## Использование

1. Создайте текстовый файл с именем proxies.txt (или любое другое имя) и добавьте в него ваши прокси в формате ip:port, например:

    ```txt
    192.168.1.1:8080
    203.0.113.5:80
    ```

2. Запустите программу, передав имя файла с прокси в качестве аргумента:

    ```shell
    python main.py proxies.txt
    ```

3. Программа выведет результаты проверки прокси в консоль, показывая, какие прокси работают, а какие нет.

## Пример вывода

```shell
Загружено 2 прокси из файла 'proxies.txt'.
Прокси 192.168.1.1:8080 работает! Ответ: {'origin': '192.168.1.1'}
Прокси 203.0.113.5:80 не работает! Код ответа: 403
```

## Зависимости

- requests: для выполнения HTTP-запросов.
- colorama: для цветного вывода в консоли.

## Лицензия

Этот проект лицензирован на условиях MIT License.

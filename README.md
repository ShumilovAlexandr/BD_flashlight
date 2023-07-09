# Задания.
### Задание №1.
Необходимо было спроектировать базу данных согласно ТЗ, без описания бизнес-логики. Результатом должна быть схема, и SQL запросы для получения: 
2.1. Информации о сумме товаров заказанных под каждого клиента (Наименование клиента, сумма)
2.2. Найти количество дочерних элементов первого уровня вложенности для категорий номенклатуры.
### Результат по заданию №1.
В модуле под названием database_test/database размещены следующие файлы:
1) create_tables.py - тут отображена структура предлагаемой базы данных (таблицы);
2) SQL-script.py - тут приведены скрипты, отвечающие на поставленные задачи;
3) Остальные файлы оставлены опционально, так как создавалась база данных и проверялись вышеуказанные скрипты в действии.

### Задание №2.
Фонарь (тестовое задание) <br>
Требуется написать управляемый по сети фонарь. <br>
Команды управления фонарь принимает от сервера фонаря. Предполагается, что 
реализация сервера уже
существует (однако недоступен вам в процессе разработки клиента фонаря). Фонарь
и сервер общаются по Протоколу Управления Фонарем (ПУФ), работающему поверх
соединения TCP.
ПУФ устроен следующим образом. Для изменения состояния фонаря сервер
передает ему команду управления. Все команды передаются в формате json вида:
{
 "command" = text,
 "metadata" = double
}
ПУФ версии 1 описывает три команды:
• ON (включить фонарь),
• OFF (выключить фонарь)
• COLOR (сменить цвет)
Цвет (при необходимости) кладется в поле метадата.
Реализация фонаря должна удовлетворять следующим требованиям:
1. При запуске фонарь должен запрашивать хост:порт (по умолчанию
127.0.0.1:9999), подсоединяться по TCP и после этого начать
отрабатывать протокол управления.
2. При получении данных от сервера фонарь проверяет команду,
и, если она известна, обрабатывает команду, иначе молча ее игнорирует.
3. При получении команды ON фонарь включается (отрисовку
фонаря оставляем на ваше усмотрение).
4. При получении команды OFF фонарь выключается.
5. При получении команды COLOR фонарь меняет цвет.
6. При завершении работы фонарь корректно закрывает соединение
с сервером.
7. Реализация фонаря позволяет легко добавлять любые новые команды.
Проработанность обработки исключительных ситуаций (ошибки установления соединения, обрывы соединения) — на ваше усмотрение.
#### Технологические требования:
1. Задание принимается в виде готового к выполнению Python-пакета.
Обязательно наличие инструкции по запуску.
2. Версия Python — 3.7+.
3. Реализация сетевого протокола может быть на aiohttp, tornado или fastAPI.
4. Репозиторий с исходниками должен быть доступен на GitHub или GitLab.

#### Как проверить готовый результат по заданию №2.
1) Склонировать проект себе на локальную машину командой git clone https://github.com/ShumilovAlexandr/BD_flashlight;
2) Выполнить установку виртуального окружения внутри проекта в корневой директории командой python -m venv venv;
3) Запустить виртуальное окружение командой  .\venv\Scripts\activate;
4) Перейти в модуль с заданием №2 командой cd flashlight-test;
5) Запустить проект командой python .\application.py
6) Перейти по пути http://127.0.0.1:9999
7) В браузере перейти в консоль в инструментах разработчика (например, просмотреть код -> консоль, если в качестве клиента используете браузер Google Chrome), там увидите сообщение, что WebSocket соединение установлено.
8) Начать тестирование приложения, посылая следующие
   а) команды: ws.send(JSON.stringify({"command": "ON"})) - для включения фонаря;
   б) ws.send(JSON.stringify({"command": "OFF"})) - для выключения фонаря;
   в) ws.send(JSON.stringify({"command": "COLOR", "metadata": "red"})) - для смены цвета фонаря (цвет red указан в качестве примера).

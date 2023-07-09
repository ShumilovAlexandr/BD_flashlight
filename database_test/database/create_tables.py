from abc import (ABC,
                 abstractmethod)

from init_db import create


class CreateTables(ABC):
    """
    Абстрактный класс для дальнейшего создания классов.
    """

    def __init__(self):
        self.connection = create.get_connection()

    @abstractmethod
    def create_table(self):
        pass


class CreateNomenclature(CreateTables):
    """Класс для создания таблицы номенклатуры товара."""

    def __init__(self):
        super().__init__()

    def create_table(self):
        """
        Функция создает таблицу со следующими колонками:
        id - заполняются автоматически;
        name - название номенклатуры товара;
        count - количество товара в номенклатуре;
        price - цена 1 единицы с плавающей точкой (2 знака после запятой).
        :return:
        """
        cursor = self.connection
        cursor.execute('CREATE TABLE nomenclature ('
                       'id serial primary key, '
                       'name varchar, '
                       'count integer, '
                       'price decimal (50, 2))')
        cursor.close()


class CreateCatalog(CreateTables):
    """Класс для создания таблицы каталога товаров."""
    def __init__(self):
        super().__init__()

    def create_table(self):
        """
        Функция создает таблицу со следующими колонками:
        id - заполняются автоматически;
        name - название категории (каталога);
        parent_id - ссылка на родительский идентификатор (для создания
        иерархии).
        :return:
        """
        cursor = self.connection
        cursor.execute('CREATE TABLE catalog ('
                       'id serial primary key,'
                       'nomenclature_id integer references nomenclature(id), '
                       'name varchar,'
                       'parent_id integer references catalog(id))')
        cursor.close()


class CreateClient(CreateTables):
    """Класс для создания таблицы клиентов."""
    
    def __init__(self):
        super().__init__()

    def create_table(self):
        """
        Функция создания таблицы с колонками:
        id - заполняются автоматически;
        name - название клиента (имя клиента);
        address - адрес клиента.
        :return:
        """
        cursor = self.connection
        cursor.execute('CREATE TABLE clients '
                       '(id serial primary key,'
                       'name varchar(50) not null, '
                       'address varchar (250))')
        cursor.close()


class CreateOrders(CreateTables):
    """Класс для создания таблицы заказов."""

    def __init__(self):
        super().__init__()

    def create_table(self):
        """
        Функция создания таблицы с колонками:
        id - заполняются автоматически;
        id_client - id клиента (связка на существующего клиента);
        item_count - количество единиц заказываемого товара;
        price - это цифровое значение, ссылвающееся на значение
        nomenclature (id), по которому можно получать значение.
        :return:
        """
        cursor = self.connection
        cursor.execute('CREATE TABLE orders ('
                       'id serial primary key,'
                       'id_client integer references clients(id),'
                       'item_count integer, '
                       'price integer references nomenclature (id))')
        cursor.close()


if __name__ == '__main__':
    """Запускаем создание таблиц."""
    nomenclature = CreateNomenclature().create_table()
    catalog = CreateCatalog().create_table()
    clients = CreateClient().create_table()
    orders = CreateOrders().create_table()

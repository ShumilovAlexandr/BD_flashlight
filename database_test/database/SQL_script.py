import pandas as pd

from init_db import create


def print_data(info):
    data = pd.DataFrame(info)
    print(data)


def get_sum_and_clients():
    """Запрос возвращает сумму товаров для каждого клиента."""
    conn = create.get_connection()
    conn.execute(
        "select clients.name, sum(nomenclature.price * orders.item_count) "
        "from clients, nomenclature, orders "
        "where orders.id_client = clients.id "
        "and orders.price = nomenclature.id "
        "group by clients.name")
    table_check = conn.fetchall()
    conn.close()
    print_data(table_check)


def get_count_element():
    """
    Запрос возвращает количество дочерних элементов первого уровня
    вложенности для категорий номенклатуры.
    """
    conn = create.get_connection()
    conn.execute("select count(name) from catalog where parent_id is null")
    check = conn.fetchall()
    conn.close()
    print_data(check)


get_sum_and_clients()
get_count_element()

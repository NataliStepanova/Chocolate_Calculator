import psycopg2
from Keys import DATABASE_PASSWORD


def get_recipes():
    try:
        conn = psycopg2.connect(
            dbname='Chocolate', user='postgres', password=DATABASE_PASSWORD, port='5432')
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    'SELECT choc_recipes_id, name, total_gramm, proc_kakao, proc_maslo FROM public.choc_recipes')
                data = cursor.fetchall()
                conn.close()
                return data
        finally:
            conn.close()
    except:
        print('Ошибка подключения к базе данных')


def put_recipe(current_recipe, recipe_name):
    try:
        conn = psycopg2.connect(
            dbname='Chocolate', user='postgres', password=DATABASE_PASSWORD, port='5432')
        try:
            data_for_db = str(current_recipe['vsego']) + ', ' + str(
                current_recipe['proc_kakao']) + ', ' + str(current_recipe['proc_maslo'])
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO choc_recipes VALUES (DEFAULT, '" + recipe_name + "', " + data_for_db + ")")
                conn.commit()
                conn.close()

        finally:
            conn.close()
    except:
        print('Ошибка подключения к базе данных')

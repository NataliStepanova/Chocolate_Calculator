import psycopg2
from Keys import DATABASE_PASSWORD


def get_recipes():
    try:
        conn = psycopg2.connect(
            dbname='Chocolate', user='postgres', password=DATABASE_PASSWORD, port='5432')
        # cursor = conn.cursor()
        # print('Соединение произведено...')
        # cursor.close()  # закрываем курсор
        # conn.close()  # закрываем соединение
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    'SELECT chocolate_recipes_id, name_recipe, total_gramm, "% kakao", "% maslo" FROM public.chocolate_recipes')
                data = cursor.fetchall()
                conn.close()
                return data
                # insert_query = "INSERT INTO 'chocolate_recipes' () '
        finally:
            conn.close()
    except:
        print('Ошибка подключения к базе данных')

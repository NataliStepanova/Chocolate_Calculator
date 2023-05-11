import psycopg2
from Keys import DATABASE_PASSWORD
# Дропни таблицу и создай заново с ИД авто инкремент!

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
        finally:
            conn.close()
    except:
        print('Ошибка подключения к базе данных')

def put_recipe(current_recipe):
    try:
        conn = psycopg2.connect(
            dbname='Chocolate', user='postgres', password=DATABASE_PASSWORD, port='5432')
        # cursor = conn.cursor()
        # print('Соединение произведено...')
        # cursor.close()  # закрываем курсор
        # conn.close()  # закрываем соединение
        # 3, 'dark_2', 85, 51, 17, 17, 60, 20, 17.96, 'Puh'
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO chocolate_recipes VALUES (5, 'dark_10', 85, 42.5, 42.5, 50, 50, 0, 43.3, 'Pin')")  
                conn.commit()
                conn.close()
                
        finally:
            conn.close()
    except:
        print('Ошибка подключения к базе данных')
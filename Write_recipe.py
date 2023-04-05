import os.path
from Create_pdf.Create_pdf import create_pdf


def write_recipe(vsego: int, kakao: int, maslo: int, pudra: int, fat_vsego: int):

    ask_filename = input('Задайте имя, чтобы сохранить рецепт: ')
    if len(ask_filename) < 1:
        print('Спасибо за использование нашей программы!')
        exit(0)

    path = './recipes/' + ask_filename + '.pdf'

    is_file_exists = os.path.exists(path)

    if is_file_exists:
        ask_rewrite = input('Такой файл существует - перезаписать? (Y/N)')
        if ask_rewrite == 'y' or ask_rewrite == 'yes' or ask_rewrite == 'Yes' or ask_rewrite == 'YES' or ask_rewrite == 'Да' or ask_rewrite == 'да' or ask_rewrite == 'Д' or ask_rewrite == 'д':
            create_pdf(vsego, kakao, maslo,
                       pudra, fat_vsego, ask_filename)
        else:
            write_recipe(vsego, kakao, maslo,
                         pudra, fat_vsego)

    else:
        create_pdf(vsego, kakao, maslo,
                   pudra, fat_vsego, ask_filename)

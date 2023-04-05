from Print_recipe import print_recipe_in_console
from Create_pdf.Create_pdf import create_pdf

gr_vsego = int(input('Укажите вес готового продукта(гр) '))
proc_kakao = int(input('Укажите % какао (гр) '))
proc_maslo = int(input('Укажите % какао-масла (гр) '))
KAKAO_FAT_PERCENT = 10
if proc_kakao + proc_maslo > 100:
    print('Уменьшите количество какао-масла ')
    exit(0)

odin_proc = (gr_vsego / 100)
gr_kakao = round(proc_kakao * odin_proc, 2)
# кол-во масла (gr_maslo) это и есть 100% жира
gr_maslo = round(proc_maslo * odin_proc, 2)
gr_pudra = round(gr_vsego - (gr_kakao + gr_maslo), 2)
fat_gr_kakao = round(gr_kakao / KAKAO_FAT_PERCENT, 2)
fat_gr_vsego = round(fat_gr_kakao + gr_maslo, 2)

print_recipe_in_console(gr_vsego, gr_kakao, gr_maslo, gr_pudra, fat_gr_vsego)

ask_filename = input('Задайте имя, чтобы сохранить рецепт: ')
if len(ask_filename) < 1:
    print('Спасибо за использование нашей программы!')
    exit(0)

create_pdf(gr_vsego, gr_kakao, gr_maslo, gr_pudra, fat_gr_vsego, ask_filename)

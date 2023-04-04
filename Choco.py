import jinja2
import pdfkit
gr_vsego = int(input('Укажите вес готового продукта(гр) '))
proc_kakao = int(input('Укажите % какао (гр) '))
proc_maslo = int(input('Укажите % какао-масла (гр) '))
KAKAO_FAT_PERCENT = 10
if proc_kakao + proc_maslo > 100:
    print('Уменьшите количество какао-масла ')
    exit(0)

odin_proc = (gr_vsego / 100)
gr_kakao = round(proc_kakao * odin_proc, 2)
gr_maslo = round(proc_maslo * odin_proc, 2)
gr_pudra = round(gr_vsego - (gr_kakao + gr_maslo), 2)
fat_gr_kakao = round(gr_kakao / KAKAO_FAT_PERCENT, 2)
# кол-во масла (gr_maslo) это и есть 100% жира

fat_gr_vsego = round(fat_gr_kakao + gr_maslo, 2)
print('Для приготовления ' + str(gr_vsego) + ' грамм шоколада понадобится: \n' + 'Вес какао-бобов ' + str(gr_kakao) + ' \n' +
      'Вес какао-масла ' + str(gr_maslo) + ' \n' + 'Вес сахарной пудры ' + str(gr_pudra))
# массовую долю жира ограничить 2мя знаками
print('Массовая доля жира: ' + str(fat_gr_vsego))

ask_filename = input('Если вы хотите сохранить рецепт - задайте имя: ')
if len(ask_filename) < 1:
    print('Спасибо за использование нашей программы!')
    exit(0)

data_for_template = {
    'gr_vsego': str(gr_vsego),
    'gr_kakao': str(gr_kakao),
    'gr_maslo': str(gr_maslo),
    'gr_pudra': str(gr_pudra),
    'fat_gr_vsego': str(fat_gr_vsego)
}

template_loader = jinja2.FileSystemLoader('./')

template_env = jinja2.Environment(loader=template_loader)

template = template_env.get_template('Template.html')

output_text = template.render(data_for_template)

config = pdfkit.configuration(
    wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
pdfkit.from_string(
    output_text, './recipes/pdf_generated.pdf', configuration=config)

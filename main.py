from Print_recipe import print_recipe_in_console, print_recipe_in_window
from Write_recipe import write_recipe
from Ingredients import Kakao
from Ingredients import Maslo
from Ingredients import Pudra
import PySimpleGUI as psg

psg.theme('DarkBrown5')
layout = [[psg.Text('Укажите вес готового продукта (гр): '), psg.InputText(key='gr_vsego')],
          [psg.Text('Укажите % какао (гр): '),
           psg.InputText(key='proc_kakao')],
          [psg.Text('Укажите % какао-масла (гр): '),
           psg.InputText(key='proc_maslo')],
          [psg.Text("", size=(60, 10), key='Recipe')],
          [psg.Button('Посчитать!'), psg.Button('Отмена')]]

window = psg.Window('Калькулятор шоколада', layout)
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == 'Отмена':  # if user closes window or clicks cancel
        break

    gr_vsego = int(values['gr_vsego'])
    proc_kakao = int(values['proc_kakao'])
    proc_maslo = int(values['proc_maslo'])
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
    kakao = Kakao()
    maslo = Maslo()
    pudra = Pudra()
    kakao.set_gramm(gr_kakao)
    maslo.set_gramm(gr_maslo)
    pudra.set_gramm(gr_pudra)
    common_ccal = round(kakao.ccal + maslo.ccal + pudra.ccal, 2)
    common_prot = round(kakao.prot + maslo.prot + pudra.prot, 2)
    common_fat = round(kakao.fat + maslo.fat + pudra.fat, 2)
    common_carb = round(kakao.carb + maslo.carb + pudra.carb, 2)

    print_recipe_in_console(gr_vsego, gr_kakao, gr_maslo, gr_pudra,
                            fat_gr_vsego, common_ccal, common_prot, common_fat, common_carb)
    output_recipe = print_recipe_in_window(gr_vsego, gr_kakao, gr_maslo, gr_pudra,
                                           fat_gr_vsego, common_ccal, common_prot, common_fat, common_carb)
    window['Recipe'].update(value=output_recipe)
window.close()
exit(0)


write_recipe({'vsego': gr_vsego, 'kakao': gr_kakao,
             'maslo': gr_maslo, 'pudra': gr_pudra, 'fat_vsego': fat_gr_vsego, 'ccal': common_ccal, 'prot': common_prot, 'fat': common_fat, 'carb': common_carb})

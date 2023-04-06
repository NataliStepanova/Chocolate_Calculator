from Print_recipe import print_recipe_in_console
from Write_recipe import write_recipe
from Ingredients import Kakao
from Ingredients import Maslo
from Ingredients import Pudra

gr_vsego = int(input('Укажите вес готового продукта(гр): '))
proc_kakao = int(input('Укажите % какао (гр): '))
proc_maslo = int(input('Укажите % какао-масла (гр): '))
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

write_recipe({'vsego': gr_vsego, 'kakao': gr_kakao,
             'maslo': gr_maslo, 'pudra': gr_pudra, 'fat_vsego': fat_gr_vsego, 'ccal': common_ccal, 'prot': common_prot, 'fat': common_fat, 'carb': common_carb})

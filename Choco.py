gr_vsego = int(input('Укажите вес готового продукта(гр) '))
proc_kakao = int(input('Укажите % какао (гр) '))
proc_maslo = int(input('Укажите % какао-масла (гр) '))
KAKAO_FAT_PERCENT = 10
if proc_kakao + proc_maslo > 100:
    print('Уменьшите количество какао-масла ')
    exit(0)

odin_proc = (gr_vsego / 100)
gr_kakao = proc_kakao * odin_proc
gr_maslo = proc_maslo * odin_proc
gr_pudra = gr_vsego - (gr_kakao + gr_maslo)
fat_gr_kakao = gr_kakao / KAKAO_FAT_PERCENT
# кол-во масла (gr_maslo) это и есть 100% жира
fat_gr_vsego = fat_gr_kakao + gr_maslo
print('Для приготовления ' + str(gr_vsego) + ' ' + 'грамм шоколада понадобится: \n' + 'Вес какао-бобов ' + str(gr_kakao) + ' \n' +
      'Вес какао-масла ' + str(gr_maslo) + ' \n' + 'Вес сахарной пудры ' + str(gr_pudra))
print('Массовая доля жира: ' + str(fat_gr_vsego))

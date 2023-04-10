def print_recipe_in_console(vsego, proc_kakao, proc_maslo, kakao, maslo, pudra, fatvsego, ccal, prot, fat, carb):
    print('Для приготовления ' + str(vsego) + ' грамм шоколада понадобится: \nКакао-бобов: ' + str(kakao) +
          ' грамм \nКакао-масла: ' + str(maslo) + ' грамм \nСахарной пудры: ' + str(pudra) + ' грамм')
    print('Какао-бобов % : ' + str(proc_kakao) +
          '\nКакао-масла % : ' + str(proc_maslo))
    print('Массовая доля жира %: ' + str(fatvsego))
    print('Общая калорийность на ' + str(vsego) +
          ' грамм готового шоколада: ' + str(ccal) + ' Ккал')
    print('БЖУ на ' + str(vsego) +
          ' грамм: \nБелки: ' + str(prot) + ' грамм \nЖиры: ' + str(fat) + ' грамм \nУглеводы: ' + str(carb) + ' грамм')


def print_recipe_in_window(vsego, proc_kakao, proc_maslo, kakao, maslo, pudra, fatvsego, ccal, prot, fat, carb):
    return 'Для приготовления ' + str(vsego) + ' грамм шоколада понадобится: \nКакао-бобов: ' + str(kakao) + ' грамм \nКакао-масла: ' + str(maslo) + ' грамм \nСахарной пудры: ' + str(pudra) + ' грамм\nКакао-бобов %: ' + str(proc_kakao) + '\nКакао-масла % : ' + str(proc_maslo) + '\nМассовая доля жира %: ' + str(fatvsego) + '\nОбщая калорийность на ' + str(vsego) + ' грамм готового шоколада: ' + str(ccal) + ' Ккал\nБЖУ на ' + str(vsego) + ' грамм: \nБелки: ' + str(prot) + ' грамм \nЖиры: ' + str(fat) + ' грамм \nУглеводы: ' + str(carb) + ' грамм'

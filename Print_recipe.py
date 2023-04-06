def print_recipe_in_console(vsego, kakao, maslo, pudra, fatvsego, ccal, prot, fat, carb):
    print('Для приготовления ' + str(vsego) + ' грамм шоколада понадобится: \nКакао-бобов: ' + str(kakao) +
          ' грамм \nКакао-масла: ' + str(maslo) + ' грамм \nСахарной пудры: ' + str(pudra) + ' грамм')
    print('Массовая доля жира %: ' + str(fatvsego))
    print('Общая калорийность на ' + str(vsego) +
          ' грамм готового шоколада: ' + str(ccal) + ' Ккал')
    print('БЖУ на ' + str(vsego) +
          ' грамм: \nБелки: ' + str(prot) + ' грамм \nЖиры: ' + str(fat) + ' грамм \nУглеводы: ' + str(carb) + ' грамм')

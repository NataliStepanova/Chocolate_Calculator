def transform_recipe_to_listbox(recipes):
    recipes_for_layout = []
    for recipe in recipes:
        recipes_for_layout.append(
            [recipe[0], recipe[1], str(recipe[2]) + '_гр', str(recipe[3]) + '_%_какао', str(recipe[4]) + '_%_какао-масла'])
    return recipes_for_layout

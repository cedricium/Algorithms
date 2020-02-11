#!/usr/bin/python

import math
import sys


def recipe_batches(recipe, ingredients):
    # ensure on-hand ingredients equal at least the recipe amounts
    for k, v in recipe.items():
        if k not in ingredients or v > ingredients[k]:
            return 0

    # find the smallest on-hand ingredient in the recipe
    # note: this dictates how many batches we can make
    min_ingredient = ''
    min_ing_amount = sys.maxsize

    for k, v in ingredients.items():
        if v < min_ing_amount:
            min_ingredient = k
            min_ing_amount = v

    # finally, calculate the minimum no. batches based on the smallest ing. count
    num_batches = min_ing_amount // recipe[min_ingredient]
    return num_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

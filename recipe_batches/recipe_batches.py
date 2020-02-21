#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  smallest_batch = []
  smallest = 10000000
  if len(ingredients) < len(recipe):
    return 0
  for i in recipe:
    smallest_batch.append(math.floor(ingredients[i] / recipe[i]))
    print(smallest_batch)
  for i in smallest_batch:
    if smallest > i:
      smallest = i
  return smallest 
      



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
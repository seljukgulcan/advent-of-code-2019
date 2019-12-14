import sys
from collections import defaultdict

recipe_book = dict()

# Parse Inputs
for line in sys.stdin:
    line_ing, line_out = line.strip().split(' => ')

    amount, name = line_out.split()
    amount = int(amount)

    ingredient_lst = []
    recipe_book[name] = [amount, ingredient_lst]

    list_ing = line_ing.split(', ')

    for ing in list_ing:
        amount, name = ing.split()
        amount = int(amount)

        ingredient_lst.append((name, amount))


def calc_ore(fuel=1):
    total = 0  # total amount of ore needed

    need2count = defaultdict(int)
    have2count = defaultdict(int)

    need2count['FUEL'] = fuel

    while need2count:

        for name, need_count in need2count.items():
            break

        need2count.pop(name)

        have_count = have2count[name]

        if have_count >= need_count:
            have2count[name] -= need_count
            continue

        else:
            have2count.pop(name)
            need_count -= have_count

        output_count = recipe_book[name][0]
        ingredient_lst = recipe_book[name][1]

        multiplier = need_count // output_count
        if need_count % output_count != 0:
            multiplier += 1

            excess = output_count * multiplier - need_count
            have2count[name] = excess

        # Start Converting
        for ingredient in ingredient_lst:
            ing_name, amount = ingredient

            amount *= multiplier

            if ing_name == 'ORE':
                total += amount
                continue

            ing_have_count = have2count[ing_name]
            if ing_have_count >= amount:
                have2count[ing_name] -= amount
            else:
                have2count[ing_name] = 0
                amount -= ing_have_count
                need2count[ing_name] += amount

    return total


start = 0
end = 100_000_000_000
middle = -1

while True:
    temp = (start + end) // 2
    if temp == middle:
        break
    middle = temp

    result = calc_ore(fuel=middle)

    if result > 1e12:
        end = middle
    else:
        start = middle

if result > 1e12:
    print(middle - 1)
else:
    print(middle)

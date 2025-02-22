def is_grandma_list(lst):
    def check_nested_list(sublist, products):
        for i in range(len(sublist) - 1):
            if isinstance(sublist[i], int) and isinstance(sublist[i + 1], int):
                products.add(sublist[i] * sublist[i + 1])
            elif isinstance(sublist[i], list):
                check_nested_list(sublist[i], products)

        if isinstance(sublist[-1], list):
            check_nested_list(sublist[-1], products)

    def find_adjacents(sublist):
        products = set()
        for i in range(len(sublist) - 1):
            if isinstance(sublist[i], int) and isinstance(sublist[i + 1], int):
                products.add(sublist[i] * sublist[i + 1])
            elif isinstance(sublist[i], list):
                products.update(find_adjacents(sublist[i]))

        if isinstance(sublist[-1], list):
            products.update(find_adjacents(sublist[-1]))
        return products

    products_in_nested = set()
    for elem in lst:
        if isinstance(elem, list):
            products_in_nested.update(find_adjacents(elem))

    for i in range(len(lst) - 1):
        if isinstance(lst[i], int) and isinstance(lst[i + 1], int):
            product = lst[i] * lst[i + 1]
            if product in products_in_nested:
                return True

    return False

# Test cases
print(is_grandma_list([1, 2, [[4, 5], [4, 7]], 5, 4, [[95], [2]]]))
print(is_grandma_list([5, 9, 4, [[8, 7]], 4, 7, [[5]]]))

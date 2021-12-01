def findRestaurant (list1, list2):
    results = {}
    for i in range (0, len(list1)):
        try:
            results[list1[i]] = i + list2.index(list1[i])
        except ValueError:
            continue

    minval = min(results.values())
    return [k for k, v in results.items() if v==minval]
    #return results

l1 = ["Shogun", "KFC", "Burger King"]
l2 = ["KFC", "Shogun", "Burger King"]

print(findRestaurant(l1,l2))

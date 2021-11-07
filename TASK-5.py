price = [59.45, 48.01, 598.00, 48.45, 973.5, 476.15, 145.09, 599.90, 5958.15, 5.09]
print('PART-1')
for i in price:
    r, k = map(str, str(i).split('.'))
    if len(r) == 1: r = '0'+r
    if len(k) == 1: k = '0'+k
    print(r, 'руб', k, 'коп', end=', ')

print('\nPART-2')
print(sorted(price))
print(price)

print('\nPART-3')
price_new = price.copy()
price_new.sort(reverse=True)
print(price_new)

print('\nPART-4')
print(sorted(price_new[0:5]))
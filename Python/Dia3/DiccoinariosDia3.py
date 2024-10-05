diccionario = {"a": "apple", "b": "banana", "c": "cherry"}
fruta = (diccionario["b"])
print(fruta)

dic = {'a': 1, 'b': [10,20,30], 'c': {'d': 40, 'e': 50}}
print(dic['b'][1])
print(dic['c']['d'])

print(dic.keys())
print(dic.values())

dic['f'] = 60
dic['b'].append(40)

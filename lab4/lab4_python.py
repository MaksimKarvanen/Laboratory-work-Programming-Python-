def ex1(l):
    return list(dict.fromkeys(l))

def ex2(l):
    first_max = max(l) if l else None
    second_max = None
    if first_max is not None:
        filtered_list = [x for x in l if x != first_max]
        second_max = max(filtered_list) if filtered_list else None
    return second_max

def ex3(d1, d2):
    return d1 | d2

def ex4(*t):
    return dict(t)

def ex5(d):
    return dict(sorted(d.items()))

def ex6(s):
    words = s.lower().split()
    frequency = {}
    for word in words:
        word = word.strip('.,!?;"\'()[]{}')
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency

def ex7(st1, st2):
    return st1 & st2

def ex8(t):
    return tuple(reversed(t))

def ex9(l):
    frequency = {}
    for item in l:
        frequency[item] = frequency.get(item, 0) + 1
    return max(frequency, key=frequency.get)
    

def ex10(l):
    result = []
    for item in l:
        if isinstance(item, list):
            result.extend(ex10(item))
        else:
            result.append(item)
    return result

def ex11(d, key):
    if key in d:
        return d[key]

def ex12(s):
    print(f'Original string: {s}')
    words = s.split()
    return ' '.join(sorted(set(words), key=words.index))
    
def ex13(s):
    return len(s)
        

def ex14(l):
    return [list(column) for column in zip(*l)]
    
def ex15(l1, l2):
    return zip(l1, l2)
    

print(ex1([1, 2, 2, 3, 4, 4, 5]))
print(ex2([3, 1, 4, 4, 5, 5, 5]))
print(ex3({1: 'one', 2: 'two'}, {3: 'three', 4: 'four'}))
print(ex4((1, 'one'), (2, 'two'), (3, 'three')))
print(ex5({3: 'three', 1: 'one', 2: 'two'}))
print(ex6("Hello, hello! How are you? You look well."))
print(ex7({1, 2, 3}, {2, 3, 4}))
print(ex8((1, 2, 3, 4, 5)))
print(ex9([1, 2, 2, 3, 4, 4, 4, 5]))
print(ex10([1, [2, [3, 4], 5], 6, [7, 8]]))
print(ex11({'a': 1, 'b': 2, 'c': 3}, 'b'))
print(ex12("this is a test this is only a test"))
print(ex13({1, 2, 3, 4, 5}))
print(ex14([[1, 'a', 3.12], [2, 'b', 2.56], [3, 'c', -23.1]]))
print(list(ex15([1, 2, 3], ['a', 'b', 'c'])))

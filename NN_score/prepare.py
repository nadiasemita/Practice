# -*- coding: utf-8 -*-

# put there code for preparing data for modeling
global_result = set()
pairs = set()

for number in range(1, 10000):
    tuples = load(open('/home/nadia/data/triples/{}.pickle'.format(number), 'rb'))
    local_result = set()
    for _ in range(1000):
        if len(local_result) == 34:
            break
        ml_random = random.choice(tuples)
        a = ml_random[0]
        b = ml_random[1]
        if ml_random in global_result or ml_random in local_result:
            continue
        if (b, a) in pairs:
            continue
        global_result.add(ml_random)
        pairs.add((a, b))
        local_result.add(ml_random)

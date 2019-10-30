# -*- coding: utf-8 -*-
from pickle import load
import random
from CGRtools.files import SDFwrite
from CGRtools.files import SDFread


global_result = set()
pairs = set()
molecules = {}
NUMBER = set()
SIG = set()

for number in range(10, 12):
    tuples = load(open('/home/nadia/data/True_pairs_new/{}.pickle'.format(number), 'rb'))
    local_result = set()
    for _ in range(1000):
        if len(local_result) == 34:
            break
        ml_random = random.choice(tuples)
        a = ml_random[0]
        b = ml_random[1]
        sig_a = bytes(a)
        sig_b = bytes(b)
        if ml_random in global_result or ml_random in local_result:
            continue
        if (sig_b, sig_a) in pairs:
            continue
        TUPLE = (sig_a, sig_b, ml_random[2], ml_random[3])
        global_result.add(TUPLE)
        pairs.add((sig_a, sig_b))
        local_result.add(ml_random)
        if sig_a in SIG:
            pass
        else:
            molecules[sig_a] = a
        if sig_b in SIG:
            pass
        else:
            molecules[sig_b] = b
        SIG.add(sig_a)
        SIG.add(sig_b)
        if len(molecules) == 10:
            for numeric in range(20):
                if numeric in NUMBER:
                    continue
                NUMBER.add(numeric)
                with SDFwrite('{}.molecules_pickle.sdf'.format(numeric)) as f:
                    for m in molecules.values():
                        f.write(m)
                break
            molecules.clear()
with SDFread('1.molecules_pickle.sdf') as n:
    form = n.read()
    print(form)
#43401 molecules
# put there code for preparing data for modeling

# -*- coding: utf-8 -*-
from CGRtools.files import SDFwrite
from pickle import load
import random


global_result = set()
pairs = set()
molecules = {}
NUMBER = set()
SIG = set()


def get_set(path, number, n):
    for num in range(number):
        tuples = load(open('{}/{}.pickle'.format(path, num), 'rb'))
        local_result = set()
        for _ in range(1000):
            if len(local_result) == n:
                break
            ml_random = random.choice(tuples)
            a = ml_random[0]
            b = ml_random[1]
            sig_a = bytes(a)
            sig_b = bytes(b)
            if ml_random in local_result:
                continue
            if (sig_b, sig_a) in pairs:
                continue
            TUPLE = (sig_a, sig_b, ml_random[2], ml_random[3])
            global_result.add(TUPLE)
            pairs.add((sig_a, sig_b))
            local_result.add(ml_random)
            if sig_a not in SIG:
                molecules[sig_a] = a
            if sig_b not in SIG:
                molecules[sig_b] = b
            SIG.update(sig_a, sig_b)
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

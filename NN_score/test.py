from pickle import load, dump
import random
from CGRtools.files import SDFwrite
from CGRtools.files import SDFread


global_result = set()
SIG = set()
NUMBER, NUMBER2, NUMBER3 = set(), set(), set()
train, test, validation = set(), set(), set()


end = False
for numeric in range(0, 43492):
    tuples = load(open('/home/nadia/data/True_pairs_new/{}.pickle'.format(numeric), 'rb'))
    for take_ml in tuples:
        a = take_ml[0]
        b = take_ml[1]
        sig_a = bytes(a)
        sig_b = bytes(b)
        TUPLE = (sig_a, sig_b, take_ml[2], take_ml[3])
        if TUPLE in global_result or (sig_b, sig_a, take_ml[2], take_ml[3]) in global_result:
            continue
        check_a = ([t[0] for t in global_result])
        check_b = ([t[1] for t in global_result])
        if (sig_b in check_b) or (sig_b in check_a) or (sig_a in check_a) or (sig_a in check_b):
            if len(validation) < len(test):
                validation.add(take_ml)
            else:
                test.add(take_ml)
        else:
            if len(test)*8 > len(train):
                train.add(take_ml)
            elif len(validation) < len(test):
                validation.add(take_ml)
            else:
                test.add(take_ml)
        global_result.add(TUPLE)
        if len(validation) == 2000:
            NUMBER.add(max(NUMBER) + 1)
            validation = validation[:1000]
            print(len(NUMBER))
            NUMBER2.add(max(NUMBER2) + 1)
            test = test[:1000]
            print(len(NUMBER2))
        if numeric == 43491 and take_ml == tuples[-1]:
            NUMBER3.add(max(NUMBER3) + 1)
            train.clear()
            print(len(NUMBER3))
            NUMBER2.add(max(NUMBER2) + 1)
            test.clear()
            print(len(NUMBER2))
            NUMBER.add(max(NUMBER) + 1)
            validation.clear()
            print(len(NUMBER))
        if len(train) == 8000:
            NUMBER3.add(max(NUMBER3)+1)
            train.clear()
            print(len(NUMBER3))
            NUMBER2.add(max(NUMBER2) + 1)
            test = test[1000:]
            print(len(NUMBER2))
            NUMBER.add(max(NUMBER) + 1)
            validation = validation[1000:]
            print(len(NUMBER))








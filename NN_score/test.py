from pickle import load, dump
import random
from CGRtools.files import SDFwrite
from CGRtools.files import SDFread


global_result, doubles = set(), set()
NUMBER, NUMBER2, NUMBER3 = {0}, {0}, {0}
train, test, validation = [], [], []
sig_train, sig_test = set(), set()


end = False
for numeric in range(0, 10000):
    tuples = load(open('/home/nadia/data/True_pairs_new/{}.pickle'.format(numeric), 'rb'))  # открываю файл
    for take_ml in tuples:
        a = take_ml[0]
        b = take_ml[1]
        sig_a = bytes(a)
        sig_b = bytes(b)
        TUPLE = (sig_a, sig_b, take_ml[2], take_ml[3])
        # проверяю, были ли такие же тюплы ранее или тюплы с помененными положениями А и Б
        if TUPLE in global_result or (sig_b, sig_a, take_ml[2], take_ml[3]) in global_result:
            continue
        check_a = ([t[0] for t in global_result])
        check_b = ([t[1] for t in global_result])
        # проверяю были ли такие же либо а, либо б ранее трайн, если были то добавляю также в трайн
        if (sig_a in sig_train) or (sig_b in sig_train):
            if (sig_a in sig_test) or (sig_b in sig_test):
                doubles.add(TUPLE)
            else:
                train.append(take_ml)
                sig_train.update((sig_a, sig_b))
        # если же а и б не встречались ранее в трайн, то добавляю в тест, вал или трайн (если ранее мы не добовляли в тест) в зависимости от их колличества
        else:
            if (sig_a in sig_test or sig_b in sig_test) or len(test)*8 < len(train):
                if len(validation) < len(test):
                    validation.append(take_ml)
                    sig_test.update((sig_a, sig_b))
                else:
                    test.append(take_ml)
                    sig_test.update((sig_a, sig_b))
            else:
                train.append(take_ml)
                sig_train.update((sig_a, sig_b))

        global_result.add(TUPLE)  # добавляю тюпл в глобал
        if len(validation) == 1000:
            print('Intersection', len(sig_train.intersection(sig_test)))
            NUMBER.add(max(NUMBER) + 1)
            validation = []
            NUMBER2.add(max(NUMBER2) + 1)
            test = []
            NUMBER3.add(max(NUMBER3) + 1)
            train = train[8000:]
            print('train:', (len(NUMBER3)-1)*8000, ' test:', (len(NUMBER2)-1)*1000,
                  ' validation:', (len(NUMBER)-1)*1000, ' doubles:', len(doubles))
        # если длина трайн достигла 8000, то сгружаем трайн полностью
        if len(train) == 16000:
            NUMBER3.add(max(NUMBER3) + 1)
            train = train[:8000]
            print('train:', (len(NUMBER3)-1)*8000, ' test:', (len(NUMBER2)-1)*1000,
                  ' validation:', (len(NUMBER)-1)*1000, ' doubles:', len(doubles))
        # когда дошли до последнего тюпла последней молекулы все сгружаем в файл
        if numeric == 43491 and take_ml == tuples[-1]:
            NUMBER3.add(max(NUMBER3) + 1)
            NUMBER2.add(max(NUMBER2) + 1)
            NUMBER.add(max(NUMBER) + 1)
            print('train:', (len(NUMBER3)-2)*8000+len(train), ' test:', (len(NUMBER2)-2)*1000+len(test),
                  ' validation:', (len(NUMBER)-2)*1000+len(validation))
            train.clear()
            test.clear()
            validation.clear()
print(len(doubles))






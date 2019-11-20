from pickle import load, dump
import random
from CGRtools.files import SDFwrite
from CGRtools.files import SDFread


global_result = set()
SIG = set()
NUMBER, NUMBER2, NUMBER3 = set(), set(), set()
train, test, validation = set(), set(), set()


end = False
for numeric in range(0, 10):
    tuples = load(open('/home/nadia/data/True_pairs_new/{}.pickle'.format(numeric), 'rb')) #открываю файл
    for take_ml in tuples:
        a = take_ml[0]
        b = take_ml[1]
        sig_a = bytes(a)
        sig_b = bytes(b)
        TUPLE = (sig_a, sig_b, take_ml[2], take_ml[3])
        if TUPLE in global_result or (sig_b, sig_a, take_ml[2], take_ml[3]) in global_result: #проверяю, были ли такие же тюплы ранее или тюплы с помененными положениями А и Б
            continue
        check_a = ([t[0] for t in global_result])
        check_b = ([t[1] for t in global_result])
        if (sig_b in check_b) or (sig_b in check_a) or (sig_a in check_a) or (sig_a in check_b): #проверяю были ли такие же либо а, либо б ранее, если были то добавляю в тест или валидейшн
            if len(validation) < len(test):
                validation.add(take_ml)
            else:
                test.add(take_ml)
        else: #если же а и б не встречались ранее, то добавляю в тест, вал или трайн в зависимости от их колличества
            if len(test)*8 > len(train):
                train.add(take_ml)
            elif len(validation) < len(test):
                validation.add(take_ml)
            else:
                test.add(take_ml)
        global_result.add(TUPLE) #добавляю тюпл в глобал
        if len(validation) == 20: #если длина вал достигла 2000, то и длина теста достигла стольо же(из условий),  сгружаю только половину тюплов из сетов
            NUMBER.add(0)
            NUMBER.add(max(NUMBER) + 1)
            validation = validation[:10] #сеты нельзя переписать!  может вернуть? for u in train[7999:]: dump(u, f) del u
            print(len(NUMBER))
            NUMBER2.add(0)
            NUMBER2.add(max(NUMBER2) + 1)
            test = test[:10]
            print(len(NUMBER2))
            NUMBER3.add(0)
        if numeric == 43491 and take_ml == tuples[-1]: #когда дошли до последнего тюпла последней молекулы все сгружаем в файл
            NUMBER3.add(max(NUMBER3) + 1)
            train.clear()
            print(len(NUMBER3))
            NUMBER2.add(max(NUMBER2) + 1)
            test.clear()
            print(len(NUMBER2))
            NUMBER.add(max(NUMBER) + 1)
            validation.clear()
            print(len(NUMBER))
        if len(train) == 80: # если длина трайн достигла 8000, то сгружаем трайн полностью, а в вал и тест 1000 первых молекул
            NUMBER3.add(max(NUMBER3) + 1)
            train.clear()
            print(len(NUMBER3))
            NUMBER2.add(max(NUMBER2) + 1)
            test = test[10:]
            print(len(NUMBER2))
            NUMBER.add(max(NUMBER) + 1)
            validation = validation[10:]
            print(len(NUMBER))










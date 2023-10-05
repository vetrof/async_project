import threading
import time

def t1():
    def loop():
        while True:
            # time.sleep(2)
            print('loop')
            pass

    t = threading.Thread(target=loop)
    t.start()

def t2():
    def loop():
        while True:
            # time.sleep(1)
            print('**********************************')
            pass

    t = threading.Thread(target=loop)
    t.start()


def t3():
    def loop():
        while True:
            # time.sleep(1)
            print('**********************************')
            pass

    t = threading.Thread(target=loop)
    t.start()


def t4():
    def loop():
        while True:
            # time.sleep(1)
            print('**********************************')
            pass

    t = threading.Thread(target=loop)
    t.start()


def t5():
    def loop():
        while True:
            # time.sleep(1)
            print('**********************************')
            pass

    t = threading.Thread(target=loop)
    t.start()

def t6():
    def loop():
        while True:
            # time.sleep(1)
            print('**********************************')
            pass

    t = threading.Thread(target=loop)
    t.start()

def t7():
    def loop():
        while True:
            # time.sleep(1)
            print('**********************************')
            pass

    t = threading.Thread(target=loop)
    t.start()


def t8():
    def loop():
        while True:
            # time.sleep(1)
            print('**********************************')
            pass

    t = threading.Thread(target=loop)
    t.start()

def t9():
    def loop():
        while True:
            # time.sleep(1)
            print('**********************************')
            pass

    t = threading.Thread(target=loop)
    t.start()

def t10():
    def loop():
        while True:
            # time.sleep(1)
            print('**********************************')
            pass

    t = threading.Thread(target=loop)
    t.start()


t1()
t2()
t3()
t4()
t5()
t6()
t7()
t8()
t9()
t10()


print('end print')

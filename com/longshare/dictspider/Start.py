#coding=utf-8
from BaseTools import *
from Spider import *


class Start:

    def startup(self):
        spider = Spinder()
        spider.login()
        time.sleep(10)
        spider.dictList()


start = Start()
start.startup()
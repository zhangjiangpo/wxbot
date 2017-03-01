#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import datetime


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.send_msg_by_uid(u'hi', msg['user']['id'])
            #self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])
'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''


def main():
    #bot = MyWXBot()
    print datetime.datetime.now()
    print time.time()
    print time.strftime('%H:%M:%S',time.localtime(time.time())) == '17:46:50'
    #bot.DEBUG = True
    #bot.conf['qr'] = 'png'
    #bot.is_big_contact = False   #如果确定通讯录过大，无法获取，可以直接配置，跳过检查。假如不是过大的话，这个方法可能无法获取所有的联系人
    #bot.run()


if __name__ == '__main__':
    main()

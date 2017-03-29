#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import datetime

import sys

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
    file_path = os.path.join(os.getcwd(),'temp/wxqr.png')
    if sys.version_info >= (3, 3):
        from shlex import quote
    else:
        from pipes import quote

    if sys.platform == "darwin":
        command = "open -a /Applications/Preview.app %s&" % quote(file_path)
        os.system(command)
    else:
        webbrowser.open(os.path.join(os.getcwd(),'temp',file_path))
    #bot = MyWXBot()
    #print datetime.datetime.now()
    #print time.time()
    #print time.strftime('%H:%M:%S',time.localtime(time.time())) == '17:46:50'
    #msg = {'content': {'data': u'\u771f\u60e8\u5440', 'type': 0, 'detail': [{'type': 'str', 'value': u'\u5443'}], 'desc': u'\u5443'}, 'msg_id': u'3060613418500156936', 'msg_type_id': 1, 'to_user_id': u'@@9899f8ca7d9dfa3512c2d238f24cd1459f262a2a8b34ef7d315bc5caf8a195ec', 'user': {'id': u'@bb22ba5cdc87071dc99aaf9d2ca03c61a0890bd6c824313ae8261fe0e17bde99', 'name': 'self'}}
    
    #contentmsg = {
    #   'group' : msg['user']['name'],
    #    'username' : msg['user']['name'],
    #    'content' : msg['content']['data'],
    #    'time' : '2017'
    #}

    #r = json.dumps(contentmsg,ensure_ascii=False)
    #print r
    #with open(os.path.join('temp','test.json'), 'a') as f:
    #            f.write(r.encode('utf-8'))
    #bot.DEBUG = True
    #bot.conf['qr'] = 'png'
    #bot.is_big_contact = False   #如果确定通讯录过大，无法获取，可以直接配置，跳过检查。假如不是过大的话，这个方法可能无法获取所有的联系人
    #bot.run()


if __name__ == '__main__':
    main()

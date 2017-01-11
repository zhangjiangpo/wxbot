#!/usr/bin/env python
# coding: utf-8
from wxbot import *

class msgForward(WXBot):
	def __init__(self):
		WXBot.__init__(self)

	def handle_msg_all(self, msg):

		if msg['msg_type_id'] == 4 and msg['content']['type'] == 0: #user send msg
			if not self.send_msg_by_uid(msg['content']['data'],self.get_user_id('龙尔尔')):
				print 'send msg error'

def main():
    bot = msgForward()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.is_big_contact = False
    bot.run()


if __name__ == '__main__':
    main()



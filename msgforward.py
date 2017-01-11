#!/usr/bin/env python
# coding: utf-8
from wxbot import *
import os

class msgForward(WXBot):
	def __init__(self):
		WXBot.__init__(self)

	def handle_msg_all(self, msg):

		username = self.get_user_id('龙尔尔');

		if msg['msg_type_id'] == 37 and msg['content']['type'] == 37: #user add request
			
			if not self.apply_useradd_requests(msg['content']['data']):
				print 'add friend error'

		if msg['msg_type_id'] == 4 and msg['content']['type'] == 0 : #user send msg
			if not self.send_msg_by_uid(msg['content']['data'],username):
				print 'send msg error'

		if msg['msg_type_id'] == 4 and msg['content']['type'] == 3 : #user send img
			imgpath = self.get_msg_img(msg['msg_id'])
			print imgpath
			if not self.send_img_msg_by_uid(os.path.join(self.temp_pwd,imgpath),username):
				print 'send msg error'

def main():
    bot = msgForward()
    #bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.is_big_contact = False
    bot.run()


if __name__ == '__main__':
    main()



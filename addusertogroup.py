#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import datetime
import re


class AddUserToGroup(WXBot):
	def __init__(self):
		WXBot.__init__(self)
	
	def writeFile(self,msg):
		d = datetime.date.today()
		f = open('./errorlog/' + d + '.json','a+')
		f.write(msg)
		f.close();
	
	def getGroupName(self,groupname):

		temp = groupname.decode('utf8')  
		xx=u"([/u4e00-/u9fa5]+)"
		pattern = re.compile(xx)
		results =  pattern.findall(temp)
		resu = ''
		for result in results :
			resu = resu + result
		return resu

	def addToGroup(self,userid,groupname):

		if not self.add_friend_to_group(userid,groupname):
			if not self.invite_friend_to_group(userid,groupname):
				return False
		return True
	
	def handle_msg_all(self, msg):
		
		group_name = self.to_unicode('测试群')

		msg['errortype'] = ''

		if msg['msg_type_id'] == 37 and msg['content']['type'] == 37: #user add request
			
			if self.apply_useradd_requests(msg['content']['data']):
				print msg['user']['id']
				print group_name
				if not self.addToGroup(msg['user']['id'],group_name):
					msg['errortype'] = 'addtogroup'
				
			else:
				msg['errortype'] = 'addfriend'

		#if msg['msg_type_id'] == 4 and msg['content']['type'] == 0: #user send msg
			#if not self.addToGroup(msg['user']['id'],group_name):
				#msg['errortype'] = 'addtogroup'

		if msg['errortype'] != '':
				self.writeFile(msg)


def main():
    bot = AddUserToGroup()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.is_big_contact = False
    bot.run()


if __name__ == '__main__':
    main()



#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import datetime
import re


class xhcMain(WXBot):
	def __init__(self):
		WXBot.__init__(self)
	
	def writeFile(self,msg):
		d = datetime.date.today()
		f = open('./errorlog/' + d + '.json','a+')
		f.write(msg)
		f.close();

	def addToGroup(self,userid,groupname):

		if not self.add_friend_to_group(userid,groupname):
			if not self.invite_friend_to_group(userid,groupname):
				return False
		return True
	
	def handle_msg_all(self, msg):
		
		msg['errortype'] = ''
		print msg

		if msg['msg_type_id'] == 371 and msg['content']['type'] == 371: #user add request
			if len(self.contact_list) > 4000:
				print '联系人数量超过4000！！'

			if self.apply_useradd_requests(msg['content']['data']):
				print msg['user']['id']
				print group_name

				if len(self.group_list) == 0:
					print 'group number 0'


				if not self.addToGroup(msg['user']['id'],group_name):
					msg['errortype'] = 'addtogroup'
				
			else:
				msg['errortype'] = 'addfriend'

		#if msg['msg_type_id'] == 4 and msg['content']['type'] == 0: #user send msg
			#if not self.addToGroup(msg['user']['id'],group_name):
				#msg['errortype'] = 'addtogroup'

		if msg['errortype'] != '':
				self.writeFile(msg)

		if msg['msg_type_id'] == 4 and msg['content']['type'] == 0: #normal msg
			uids = [];
			for user in self.contact_list:
				if user["NickName"] == self.to_unicode("宁波") or user["NickName"] == self.to_unicode("小红唇测试") :
					print user
					uids.append(user["UserName"])

			if not self.create_group(uids):
				msg['errortype'] = 'create group filed'

		if msg["msg_type_id"] == 3 and msg['content']['type'] == 12: #group admin add/delete member
			# msg['user']['id']    #group ID 变化的 与 self.group_list的UserName 相对  与 self.group_members的key相对（key是属性值） 存NickName到数据库
			# msg['user']['name']  #group name 固定的（管理员可改变） 与 self.group_list的NickName 相对
			self.get_contact(); #添加/删除 改名 重新初始化数据
			self.batch_get_group_members() #批量获取所有群聊成员信息
			print self.group_list
			print '>>>>>>>>>>>>>>>>>>>>>>>'
			print '>>>>>>>>>>>>>>>>>>>>>>>'
			print self.group_members




def main():
    bot = xhcMain()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.is_big_contact = False
    bot.run()


if __name__ == '__main__':
    main()


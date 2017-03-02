#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import datetime
import re
import requests
import json



class xhcMain(WXBot):
	def __init__(self):
		WXBot.__init__(self)

	def handle_data(self,gid,gname):
		return {'name':gname,'botname':self.my_account['NickName'],'number':len(self.group_members[gid]),'oldname':''}

	def self_request(self,url,data):
		d = requests.post('http://gzh.xiaohongchun.com/'+url,data = data)
		#print d.json()
		if d.status_code != 200:#请求失败
			print 'failed: ' + url
		else:
			print 'success:' + url

	def login_success_init(self):#机器人初始化 遍历所有群组 发送服务器同步数据
		for g in self.group_list:
			time.sleep(2)
			#print "<<<<<<<<<<init group info>>>>>>>>>>"
			self.self_request('api/group/inputinfo',self.handle_data(g['UserName'],g['NickName']))

	def timediff(self,timestr,timeformat = '%H:%M:%S'):
		#print time.strftime(timeformat,time.localtime(time.time()))
		#print timestr
		return time.strftime(timeformat,time.localtime(time.time())) == timestr
	
	def handle_msg_all(self, msg):
		
		print msg

		#if msg['msg_type_id'] == 4 and msg['content']['type'] == 0: #normal msg
			#uids = [];
			#for user in self.contact_list:
				#if user["NickName"] == self.to_unicode("宁波") or user["NickName"] == self.to_unicode("小红唇测试") :
					#print user
					#uids.append(user["UserName"])

			#if not self.create_group(uids):
				#msg['errortype'] = 'create group filed'

		if msg["msg_type_id"] == 3 and msg['content']['type'] == 12: #group admin add/delete member
			# msg['user']['id']    #group ID 变化的 与 self.group_list的UserName 相对  与 self.group_members的key相对（key是属性值） 存NickName到数据库
			# msg['user']['name']  #group name 固定的（管理员可改变） 与 self.group_list的NickName 相对
			self.get_contact(); #添加/删除 改名 重新初始化数据
			self.batch_get_group_members() #批量获取所有群聊成员信息
			print '<<<<<<<<<<<<<<<<<<group list>>>>>>>>>>>>>>>>>>>>>>>'
			print self.group_list
			print '<<<<<<<<<<<<<<<<<<group member list>>>>>>>>>>>>>>>>>>>>>>>'
			print len(self.group_members[msg['user']['id']])

			data = {}

			for g in self.group_list:
			
				if g['UserName'] == msg['user']['id']: 
			
					data = self.handle_data(g['UserName'],g['NickName'])

					data['oldname'] = msg['user']['name']

			#print '<<<<<<<<<<<<<<<<<<group change data>>>>>>>>>>>>>>>>>>>>>>';
			#print data;

			self.self_request('api/group/changeinfo',data);

	def schedule(self):#定时触发 频率26s

		if self.timediff('10','%S'):#一分钟的第十秒刷新一次
			self.login_success_init();#定时刷新数据

		#if self.timediff('18:10:00'):#每天18点

			#for g in self.group_list:#向所有群组发送信息

				#self.send_msg_by_uid('测试,请忽略！！定时任务', g['UserName'])

		#time.sleep(2) #单位s

def main():
    bot = xhcMain()
    bot.DEBUG = False
    bot.conf['qr'] = 'png'
    bot.is_big_contact = False
    bot.run()


if __name__ == '__main__':
    main()


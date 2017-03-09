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

	def handle_data(self,gname,gid,number,oldname):
		return {'name':gname,'botname':self.my_account['NickName'],'number':number,'oldname':oldname}

	def self_request(self,url,data):
		d = requests.post('http://gzh.xiaohongchun.com/'+url,data = data)
		#print d.json()
		if d.status_code != 200:#请求失败
			print 'failed: ' + url
		else:
			print 'success:' + url

	def login_success_init(self):#机器人初始化 遍历所有群组 发送服务器同步数据

		for g in self.group_list_data:
			if g['UserName'].find('@@') != -1:
				print g['NickName']
				#time.sleep(2)
				#print "<<<<<<<<<<init group info>>>>>>>>>>"
				#self.self_request('api/group/inputinfo',self.handle_data(g['NickName'],g['UserName'],len(g['MemberList']),''))

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
			
			data = {}
			oldname = ''

			for g in self.group_list_data:
			
				if g['UserName'] == msg['user']['id']: 

					oldname = g['NickName']

			self.getInitData();#自定义方法 更新群组信息

			for g in self.group_list_data:
			
				if g['UserName'] == msg['user']['id']:
			
					data = self.handle_data(g['NickName'],g['UserName'],len(g['MemberList']),oldname)

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


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
		d = requests.post('http://127.0.0.1:8010/'+url,data = data)
		#print d.json()
		if d.status_code != 200:#请求失败
			print 'failed: ' + url
		else:
			print 'success:' + url

	def login_success_init(self):#机器人初始化 遍历所有群组 发送服务器同步数据
		self.get_contact(); #添加/删除 改名 重新初始化数据
		self.batch_get_group_members() #批量获取所有群聊成员信息
		for g in self.group_list:
			time.sleep(2)
			#print "<<<<<<<<<<init group info>>>>>>>>>>"
			self.self_request('api/group/inputinfo',self.handle_data(g['UserName'],g['NickName']))

	def timediff(self,timestr,timeformat = '%H:%M:%S'):
		#print time.strftime(timeformat,time.localtime(time.time()))
		#print timestr
		return time.strftime(timeformat,time.localtime(time.time())) == timestr

	def gettime(self, timeformat = '%Y-%m-%d'):
		return time.strftime(timeformat,time.localtime(time.time()))
	
	def handle_msg_all(self, msg):
		
		print msg;

		if (msg['msg_type_id'] == 3 or msg['msg_type_id'] == 1) and msg['content']['type'] == 0: #normal msg 1 self 3 other
			username = ''
			if msg['msg_type_id'] == 1:
				username = self.my_account['NickName']
			else:
				username = msg['content']['user']['name']
			contentmsg = {
				'group' : msg['user']['name'],
				'username' : username,
				'content' : msg['content']['data'],
				'time' : self.gettime('%Y-%m-%d %H:%M:%S')
			}
			r = json.dumps(contentmsg,ensure_ascii=False)
			r = r + ','
			with open(os.path.join(self.temp_pwd,self.gettime() + 'groupmsg.json'), 'a') as f:
				f.write(r.encode('utf-8'))
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

			data = {}

			for g in self.group_list:
			
				if g['UserName'] == msg['user']['id']: 
			
					data = self.handle_data(g['UserName'],g['NickName'])

					data['oldname'] = msg['user']['name']

			timejg = self.group_welcome.get(msg['user']['id']);
			
			if data['oldname'] == data['name'] and (timejg == None or timejg < time.time()):#不是修改群名称 新增人员

				self.group_welcome[msg['user']['id']] = time.time() + 120;

				if not self.send_msg_by_uid(' 欢迎加入“天天跟我买-VIP群”\n 👏👏👏\n✋✋这里可以让你即时获取全网【白菜价】和【历史新低】的好物资讯，并提供一键代买服务～ \n 也可以 @天天君 帮你找到最合适的产品！\n\n 🎁🎁🎁附赠绝密信息一份：转发本条信息下的文字和图片到朋友圈并截屏发送在群内@天天君 ，即可参与每周【免单】活动！\n\n 查看更多限时优惠关注我们的微信小程序“天天跟我买”\n 【小程序打开方式：微信--发现---小程序---搜索“天天跟我买”】',msg['user']['id']):

					print 'send msg1 error'

				time.sleep(1);

				if not self.send_msg_by_uid(' 卧槽！刚发现以前买的东西全尼玛买贵了[捂脸] 纸抽9毛！iphone数据线2块9！YSL#407唇釉193！阿迪绿尾小白鞋379！[捂脸][捂脸][捂脸] 全在这里！在这里！这里！里！ ↓↓↓↓↓↓↓',msg['user']['id']):

					print 'send msg2 error'

				time.sleep(1);

				if not self.send_img_msg_by_uid(os.path.join(self.temp_pwd,'joingroup.jpg'),msg['user']['id']):
					
					print 'send msg error'

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


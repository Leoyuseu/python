# -*- coding:utf-8 -*-
# file: server.py
#
import Tkinter
import threading
import socket
class ListenThread(threading.Thread):	         #监听线程				# 创建监听线程
	def __init__(self,edit,server):
		threading.Thread.__init__(self)
		self.edit = edit							# 保存窗口中的多行文本框
		self.server = server
	def run(self):				#进入监听状态				# 进入监听状态
		while 1:			#等待连接					# 使用while循环不停监听
			try:								# 捕获异常
				client, addr = self.server.accept()  			# 等待连接
				self.edit.insert(Tkinter.END,				# 向文本框中输出状态
						'连接来自:%s:%d\n' % addr)
				data = client.recv(1024)				# 接受数据
				self.edit.insert(Tkinter.END, 				# 向文本框中输出数据
						'收到数据:%s \n' % data)
				client.send('I GOT: %s' % data)				# 发送数据
				client.close()						# 关闭同客户端的连接
				self.edit.insert(Tkinter.END,				# 向文本框中输出状态
						'关闭客户端\n')
			except:							        # 异常处理
				self.edit.insert(Tkinter.END,				# 向文本框中输出状态
						'关闭连接\n')
				break							# 结束循环
class Control(threading.Thread):							# 控制线程
	def __init__(self, edit):  
		threading.Thread.__init__(self)
		self.edit = edit							# 保存窗口中的多行文本框
		self.event = threading.Event()						# 创建Event对象
		self.event.clear()							# 清楚event标志
	def run(self):  
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  		# 创建socket连接
		server.bind(('', 1051))							# 绑定本机1051端口
		server.listen(1)							# 开始监听
		self.edit.insert(Tkinter.END,'正在等待连接\n')				# 向文本框中输出状态
		self.lt = ListenThread(self.edit,server)				# 创建监听线程对象
		self.lt.setDaemon(True)
		self.lt.start()								# 执行监听线程
		self.event.wait()							# 进入等待状态
		server.close()								# 关闭连接
	def stop(self):									# 结束控制进程
		self.event.set()							# 设置event标志
class Window:										# 主窗口
	def __init__(self, root):
		self.root = root
		self.butlisten = Tkinter.Button(root, 					# 创建组件
				text = '开始监听', command = self.Listen)
		self.butlisten.place(x = 20, y = 15)
		self.butclose = Tkinter.Button(root, 
				text = '停止监听', command = self.Close)
		self.butclose.place(x = 120, y = 15)
		self.edit = Tkinter.Text(root)
		self.edit.place(y = 50)
	def Listen(self):								# 处理按钮事件
		self.ctrl = Control(self.edit)						# 创建控制线程对象
		self.ctrl.setDaemon(True)
		self.ctrl.start()							# 执行控制线程
	def Close(self):
		self.ctrl.stop()							# 结束控制线程
root = Tkinter.Tk()
window = Window(root)
root.mainloop()

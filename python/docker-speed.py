# coding:utf-8
import os
import json
step1 = "sudo mkdir -p /etc/docker"
step2 = "sudo tee /etc/docker/daemon.json <<-'EOF'\n" + json.dumps({
  'registry-mirrors': ['https://lk6og1wc.mirror.aliyuncs.com']
}) + "\n" + "EOF"
step3 = "sudo systemctl daemon-reload"
step4 = "sudo systemctl restart docker"
info = "sudo docker info"
print("执行命令:"+step1)
os.system(step1)
print("执行命名:"+step2)
os.system(step2)
print("执行命名:"+step3)
os.system(step3)
print("执行命名:"+step4)
os.system(step4)
print("加入镜像导入成功,信息如下：")
os.system(info)
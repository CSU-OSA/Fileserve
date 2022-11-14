### 阿里云OSS服务
目前为demo版
种种不足，近期完善


python需要的模块执行 pip install -r requirement.txt
还要在服务器本地部署一个mongodb (不需要设置用户密码，本地跑，不向外开放)

然后将cfg.py文件拷贝到项目根目录
服务跑起来使用到根目录 执行 python3 main.py


接口1  /api/file/upload
des:文件描述数据（英文且不能过长）
Remote-User:请求头携带的owner/name

接口2 /api/file/get_des
filename结构:owner/name/xxx.xxx 

可部署后在网址后添加 /docs 查看api文档
如本地可以直接访问 http://127.0.0.1:1001/docs

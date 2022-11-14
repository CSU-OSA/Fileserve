from fastapi import APIRouter, Header, UploadFile, File,Form
from typing import Optional
from method import Co
import db

file_route = APIRouter(
	prefix="/file",
	tags=["file"]
)


def trueReturn(data=None, msg=""):
	return {
		'status': True,
		'data': data,
		'msg': msg
	}


def falseReturn(data=None, msg=""):
	return {
		'status': False,
		'data': data,
		'msg': msg
	}





@file_route.post('/upload')
async def upload(des: str = Form(...), file: UploadFile = File(), Remote_User: Optional[str] = Header(None)):
	"""文件上传接口 demo版 \n
	des:文件描述数据（英文且不能过长） \n
	Remote-User:请求头携带的owner/name"""
	user_name = Remote_User
	byte = await file.read()
	Co.upload_file(f'{user_name}/{file.filename}', byte=byte, des=des)
	bindnum = str(db.how_much(Remote_User))
	db.fileIndex.insert_one({
		"_id": Remote_User + bindnum,
		"user_id": Remote_User,
		"filename": f'{user_name}/{file.filename}',
		"url": f"https://akashic-casdoor.oss-cn-hangzhou.aliyuncs.com/{user_name}/{file.filename}",
		"des": des
	})
	data = {
		"msg": '上传完成',
		"filename": f'{user_name}/{file.filename}',
		"url": f"https://akashic-casdoor.oss-cn-hangzhou.aliyuncs.com/{user_name}/{file.filename}"
	}
	return trueReturn(data=data)


@file_route.post('/get_des')
async def get_des(filename: str):
	""""文件查询接口 \n
	filename结构:owner/name/xxx.xxx 请务必填写清楚"""
	res = db.fileIndex.find_one({"filename": filename})
	del res["_id"]
	return trueReturn(data=res)

import oss2
import requests as r
import json
from cfg import access_id, access_key, bucket_name


class ConnectOss(object):
	def __init__(self, access_id, access_key, bucket_name):
		"""验证权限"""
		self.auth = oss2.Auth(access_id, access_key)
		self.endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'
		self.bucket = oss2.Bucket(self.auth, self.endpoint, bucket_name=bucket_name)

	def download_file(self, path, save_path):
		result = self.bucket.get_object_to_file(path, save_path)
		if result.status == 200:
			print('下载完成')

	def upload_file(self, path, byte, des):
		result = self.bucket.put_object(path, byte, headers={'x-oss-meta-des': des})
		if result.status == 200:
			print('上传完成')

	def get_msg(self, ob_name):
		simplifiedmeta = self.bucket.get_object_meta(ob_name)
		return simplifiedmeta.headers


Co = ConnectOss(access_id, access_key, bucket_name)


def getUser(id: str) -> str:
	res = r.get(f'https://auth.dev.magicalsheep.cn/api/get-user?id={id}').content
	content = json.dumps(res)
	"""请求用户数据返回数据"""
	return content['owner']+'/'+content['name']

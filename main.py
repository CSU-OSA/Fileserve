from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import cfg


def create_fastapi() -> FastAPI:
	app = FastAPI()
	# 跨域
	if cfg.cors:
		app.add_middleware(
			CORSMiddleware,

			allow_origins=["*"],

			allow_credentials=False,

			allow_methods=['*']
		)

	from router import master_router
	app.include_router(master_router)

	return app


app = create_fastapi()
if __name__ == '__main__':
	uvicorn.run(app='main:app', port=cfg.port, reload=True)

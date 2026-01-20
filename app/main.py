from  fastapi import  FastAPI
from starlette.middleware.cors import CORSMiddleware
from  app.Users.router import router as auth_router



app = FastAPI()


app.include_router(auth_router)










origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","PATH","DELETE","PUT"],
    allow_headers = ["*"] # но лучше прописывать ради безапасности

)










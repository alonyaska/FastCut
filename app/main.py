from  fastapi import  FastAPI
from starlette.middleware.cors import CORSMiddleware
from  app.Users.router import router as auth_router
from  app.URLS.router import router as link_router
from app.URLS.redirect import router as redirect_router



app = FastAPI()


app.include_router(auth_router)
app.include_router(link_router)
app.include_router(redirect_router)










origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:6666"
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","PATH","DELETE","PUT"],
    allow_headers = ["*"] # но лучше прописывать ради безапасности

)










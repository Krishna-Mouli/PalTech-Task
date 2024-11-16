from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from APIs import api_router
import uvicorn

app = FastAPI(title="paltech-pfb-assignment")

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host = "0.0.0.0", port = 8080)
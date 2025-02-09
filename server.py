from codigo import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="SecurityAI", description="Escolha um tema e obtenha respostas de qualquer framework.")

add_routes(app, chain, path="/cyber")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


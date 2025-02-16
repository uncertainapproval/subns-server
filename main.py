from fastapi import FastAPI
from routes.vertices import router as vertex_router
from routes.edges import router as edge_router

app = FastAPI(docs_url="/")
app.include_router(vertex_router)
app.include_router(edge_router)
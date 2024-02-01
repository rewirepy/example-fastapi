from fastapi import APIRouter, FastAPI
from rewire.plugins import simple_plugin

plugin = simple_plugin()
router = APIRouter(tags=["demo"])


@router.get("/hello")
def hello_world():
    return "world"


@plugin.setup()
async def include_router(app: FastAPI):
    app.include_router(router)

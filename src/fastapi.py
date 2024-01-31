from contextlib import suppress
from fastapi import FastAPI
from rewire.plugins import simple_plugin
from rewire.config import ConfigDependency
from rewire.lifecycle import LifecycleModule
import uvicorn.config

plugin = simple_plugin()


@plugin.bind
class Config(ConfigDependency):
    port: int = 8080
    title: str = "FastAPI"
    host: str = "0.0.0.0"


@plugin.setup()
async def create_fastapi(config: Config.Value) -> FastAPI:
    return FastAPI(title=config.title)


@plugin.run()
async def run(app: FastAPI, cfg: Config.Value):
    config = uvicorn.config.Config(app, port=cfg.port, host=cfg.host)
    server = uvicorn.Server(config=config)
    config.setup_event_loop()

    with suppress(LookupError):
        lm = LifecycleModule.get()

        @lm.on_stop
        async def stop():
            server.should_exit = True

    return await server.serve()

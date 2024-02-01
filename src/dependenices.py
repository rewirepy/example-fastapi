from loguru import logger
from pydantic import BaseModel
from rewire.plugins import simple_plugin

plugin = simple_plugin()


class SomeDependency(BaseModel):
    pass


@plugin.setup()
async def my_dependency() -> SomeDependency:
    return SomeDependency()


@plugin.setup()
async def my_dependency_consumer(dependency: SomeDependency):
    logger.info(f"got injected dependency: {dependency}")

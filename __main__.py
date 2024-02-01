import anyio
from rewire.dependencies import DependenciesModule
from rewire.lifecycle import LifecycleModule
from rewire.loader import LoaderModule
from rewire.space import Space
import rewire_fastapi

async def main():
    async with Space().init().use():
        DependenciesModule.get().add(rewire_fastapi.plugin)
        await LoaderModule.get().discover().load()
        await DependenciesModule.get().solve()
        await LifecycleModule.get().start()


if __name__ == "__main__":
    anyio.run(main, backend="asyncio")

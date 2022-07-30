from starlette.middleware.cors import CORSMiddleware

from _version import __version__
from fastapi import FastAPI
from src.api.router import router
from src.core.settings import settings


def get_application() -> FastAPI:
    application = FastAPI(
        title="POCemon API (🐍 FastAPI)",
        description="""This API provide list of pokemone and team management""",
        version=__version__,
        openapi_url="/openapi.json",
        docs_url="/",
        redoc_url=None,
        debug=settings().debug,
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router)
    return application

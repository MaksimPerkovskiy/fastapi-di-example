from fastapi import FastAPI
import yaml

from .controllers import router
from .providers import (
    provide_session_stub,
    provide_db,
    ProvideSession
)
from .exception_handlers import http400_error_handler


CONFIG_FILE = "config.yml"


def create_app() -> FastAPI:
    application = FastAPI()
    application.include_router(router)

    setup_di(application=application)
    setup_exception_handlers(application=application)

    return application


def read_config() -> None:
    with open(CONFIG_FILE, 'r') as file:
        return yaml.safe_load(file) 


def setup_di(application: FastAPI) -> None:
    config = read_config()
    db = provide_db(db_url=config['db']['url'])
    application.dependency_overrides[provide_session_stub] = ProvideSession(db.session_factory)


def setup_exception_handlers(application: FastAPI) -> None:
    application.add_exception_handler(ValueError, http400_error_handler)


app = create_app()

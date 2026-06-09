from fastapi import FastAPI

from app.config.settings import settings
from app.config.validators import validate_settings
from app.config.startup_checks import (
    run_startup_checks,
)

app = FastAPI(
    title="Customer Support Intelligence"
)


@app.on_event("startup")
def startup_event():

    validate_settings(settings)

    run_startup_checks(settings)
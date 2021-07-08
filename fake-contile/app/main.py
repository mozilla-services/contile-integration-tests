# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import asyncio
import logging
import sys

import yaml
from fastapi import FastAPI, HTTPException, Response, status
from models import Tiles

logger = logging.getLogger("fake_contile")

version = f"{sys.version_info.major}.{sys.version_info.minor}"


app = FastAPI()


@app.get("/")
async def read_root():
    message = (
        f"Hello world! From FastAPI running on Uvicorn "
        f"with Gunicorn. Using Python {version}"
    )
    return {"message": message}


EXAMPLE_TILES = yaml.safe_load(
    """
tiles:
  - id: 12345
    name: 'Example COM'
    click_url: 'https://example.com/desktop_windows?version=16.0.0&key=22.1&ci=6.2&ctag=1612376952400200000'
    image_url: 'https://example.com/desktop_windows01.jpg'
    impression_url: 'https://example.com/desktop_windows?id=0001'
    url: 'https://www.example.com/desktop_windows'
    position: 1
  - id: 56789
    name: 'Example ORG'
    click_url: 'https://example.org/desktop_windows?version=16.0.0&key=7.2&ci=8.9&ctag=E1DE38C8972D0281F5556659A'
    image_url: 'https://example.org/desktop_windows02.jpg'
    impression_url: 'https://example.org/desktop_windows?id=0002'
    url: 'https://www.example.org/desktop_windows'
    position: 1
"""
)


@app.get("/v1/tiles/success", response_model=Tiles, status_code=200)
async def read_tiles_success(response: Response):
    return EXAMPLE_TILES


@app.get("/v1/tiles/delay", response_model=Tiles, status_code=200)
async def read_tiles_delay(response: Response):
    # Add an artificual delay to the handler
    delay = 60 * 1 * 1
    logger.debug("response is delayed by %s seconds", delay)
    await asyncio.sleep(delay)
    return EXAMPLE_TILES


@app.get("/v1/tiles/error", response_model=Tiles, status_code=200)
async def read_tiles_error(response: Response):
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong"
    )


@app.get("/v1/tiles/invalid_content", status_code=200)
async def read_tiles_invalid_content(response: Response):
    return Response(status_code=status.HTTP_200_OK, content=",asdasd")


@app.get("/v1/tiles/no_content", status_code=status.HTTP_204_NO_CONTENT)
async def read_tiles_no_content(response: Response):
    return Response(status_code=status.HTTP_204_NO_CONTENT)

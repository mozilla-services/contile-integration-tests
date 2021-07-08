# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from typing import List

from pydantic import BaseModel


class Tile(BaseModel):
    """Class that holds information about a Tile returned by Contile."""

    id: int
    name: str
    click_url: str
    image_url: str
    impression_url: str
    url: str
    position: int


class Tiles(BaseModel):
    """Model for a list of tiles returned to Contile."""

    tiles: List[Tile]

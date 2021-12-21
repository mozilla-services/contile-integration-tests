# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from sqlalchemy.orm import Session
from . import models, db_models


def get_requests(db: Session, skip: int = 0, limit: int = 500):
    return db.query(db_models.ContileRequest).offset(skip).limit(limit).all()


def create_request(db: Session, request: Request):
    """
    creats a request and stores it in the database
    """
    contile_request = ContileRequest()
    contile_request.http_header = request.http_header
    contile_request.sub1 = request.sub1
    contile_request.sub2 = request.sub2
    contile_request.partner = request.partner
    contile_request.country_code = request.country_code
    contile_request.region_code = request.region_code
    contile_request.dma_code = request.dma_code
    contile_request.form_factor = request.form_factor
    contile_request.os_family = request.os_family
    contile_request.v = request.v
    contile_request.out = request.out
    contile_request.results = request.results

    db.add(contile_request)
    db.commit()
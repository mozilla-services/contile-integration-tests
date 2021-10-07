# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from sqlalchemy import Column, Integer, String, Numeric

from database import Base

# Creating a table structure with columns referring to query params
class RequestValue(Base):
    __tablename__ = "request_value"

    country_code = Column(String, unique=True, index=True)
    region_code = Column(String, unique=True, index=True)
    dma_code = Column(Integer, unique=True, index=True)
    form_factor = Column(String, unique=True, index=True)
    os_family = Column(String, unique=True, index=True)
    # ff_version = Column(Numeric(2,2), unique=True, index=True)

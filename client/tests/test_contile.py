# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from typing import List

import pytest
import requests
from models import Step


@pytest.fixture(name="contile_host")
def fixture_contile_host(request):
    """Read the contile host from the pytest config."""

    return request.config.option.contile_url


def test_contile(contile_host: str, steps: List[Step]):
    """Test for requesting tiles from Contile."""

    for step in steps:
        # Each step in a test scenario consists of a request and a response.
        # Use the parameters to perform the request and verify the response.

        method = step.request.method
        url = f"{contile_host}{step.request.path}"
        headers = {header.name: header.value for header in step.request.headers}

        r = requests.request(method, url, headers=headers)

        error_message = (
            f"Expected status code {step.response.status_code},\n"
            f"but the status code in the response from Contile is {r.status_code}.\n"
            f"The response content is '{r.text}'."
        )

        assert r.status_code == step.response.status_code, error_message

        if r.status_code == 200:
            # If the response status code is 200 OK, load the response content
            # into a Python dict and generate a dict from the response model
            resp = step.response.content
            if not(isinstance(resp, dict)):
                resp = resp.dict()
            assert r.json() == resp

        if r.status_code == 204:
            # If the response status code is 204 No Content, load the response content
            # as text and compare against the value in the response model. This
            # should be an empty string.
            assert r.text == step.response.content
            continue

        # If the request to Contile was not successful, load the response
        # content into a Python dict and compare against the value in the
        # response model, which is expected to be the Contile error code.
        assert r.json() == step.response.content

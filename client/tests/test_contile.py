# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
import requests


@pytest.fixture(name="contile_host")
def fixture_contile_host(request):
    """Read the contile host from the pytest config."""

    return request.config.option.contile_url


def test_contile(contile_host, steps):
    """Test for requesting tiles from Contile."""

    for step in steps:
        url = f"{contile_host}{step.request.path}"
        headers = {header.name: header.value for header in step.request.headers}

        r = requests.get(url, headers=headers)

        assert r.status_code == step.response.status_code

        if r.status_code == 200:
            # If the response status code is 200 OK, load the response content
            # into a Python dict and generate a dict from the response model
            assert r.json() == step.response.content.dict()
            continue

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
from fastapi import HTTPException
import pytest
import responses

from src.cisco.scraper.utils import get_request_forward_body


@responses.activate
def test_get_request_forward_body_if_correct_response(correct_url: str) -> None:
    # given
    url = correct_url
    response_body = {"test": "good"}
    responses.add(responses.GET, url, json=response_body, status=200)
    # when
    result = get_request_forward_body(url=url)
    # then
    assert any([isinstance(result, possible_type) for possible_type in (dict, str)])
    assert result == response_body


@responses.activate
def test_get_request_forward_body_if_request_raise_error(bad_url: str) -> None:
    # given
    url = bad_url
    response_body = ""
    responses.add(responses.GET, url, json=response_body, status=404)
    # when / then
    with pytest.raises(HTTPException):
        get_request_forward_body(url=url)

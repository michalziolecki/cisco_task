from typing import Any, Dict, Union

from fastapi import HTTPException
import requests
from requests import RequestException, Response


def get_request_forward_body(url: str) -> Union[str, Dict[str, Any]]:
    try:
        response: Response = requests.get(url)
    except RequestException:
        # TODO add logging
        raise HTTPException(status_code=400, detail=f"{url}")
    else:
        if 200 <= response.status_code < 300:
            payload_content = ""
            if "application/json" in response.headers.get("Content-Type"):
                payload_content = response.json()
            else:
                payload_content = str(response.content)
            return payload_content
        else:
            # TODO add logging
            raise HTTPException(response.status_code, detail=f"Incorrect status for address: {url}")

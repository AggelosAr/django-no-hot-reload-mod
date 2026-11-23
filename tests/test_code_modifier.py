import json
from typing import Optional, Tuple
from urllib.parse import urlencode
from urllib.request import urlopen

from tini_test import Test, must_equal


BASE_URL = "http://127.0.0.1:8000"


def request(path: str, data: Optional[dict[str, str]] = None) -> Tuple[int, str]:
    request_data = urlencode(data).encode() if data is not None else None
    with urlopen(f"{BASE_URL}{path}", data=request_data) as response:
        return response.status, response.read().decode()


@Test.case
def test_code_modifier_page_loads() -> None:
    status, page = request("/code_modifier/code_mod/")

    must_equal(200, status)
    must_equal(True, 'id="code-block-form"' in page)


@Test.case
def test_app_views_endpoint_lists_sample_view() -> None:
    status, body = request(
        "/code_modifier/get_views_for_app/?app_name=sample_app"
    )

    must_equal(200, status)
    must_equal(True, "sample" in json.loads(body)["views"])


@Test.case
def test_post_changes_sample_view_without_restarting_server() -> None:
    status, original_body = request("/sample/")
    must_equal(200, status)
    must_equal({"message": "original"}, json.loads(original_body))

    status, _ = request(
        "/code_modifier/code_mod/",
        {
            "apps": "sample_app",
            "views": "sample",
            "code_block": (
                "def replacement(request):\n"
                "    from django.http import JsonResponse\n"
                '    return JsonResponse({"message": "updated"})\n'
            ),
        },
    )
    must_equal(200, status)

    status, updated_body = request("/sample/")
    must_equal(200, status)
    must_equal({"message": "updated"}, json.loads(updated_body))

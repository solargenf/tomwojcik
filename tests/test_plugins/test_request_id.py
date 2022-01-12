from starlette import status
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.testclient import TestClient

from starlette_context import plugins
from starlette_context.header_keys import HeaderKeys
from starlette_context.middleware import ContextMiddleware
from tests.conftest import dummy_request_id

middleware = [
    Middleware(
        ContextMiddleware,
        plugins=(plugins.RequestIdPlugin(),),
    )
]
app = Starlette(middleware=middleware)
client = TestClient(app)
headers = {HeaderKeys.request_id: dummy_request_id}


@app.route("/")
async def index(request: Request) -> Response:
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def test_valid_request_returns_proper_response():
    response = client.get("/", headers=headers)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.headers.get(HeaderKeys.request_id) == dummy_request_id


def test_invalid_request_id_returns_a_bad_request():
    response = client.get("/", headers={HeaderKeys.request_id: "invalid_uuid"})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert HeaderKeys.request_id not in response.headers


def test_missing_header_will_assign_one():
    response = client.get("/", headers={})
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert HeaderKeys.request_id in response.headers


def test_force_new_uuid():
    app_force_uuid = Starlette(
        middleware=[
            Middleware(
                ContextMiddleware,
                plugins=(plugins.RequestIdPlugin(force_new_uuid=True),),
            )
        ]
    )
    force_uuid_client = TestClient(app_force_uuid)

    @app_force_uuid.route("/")
    async def index(request: Request) -> Response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    response = force_uuid_client.get("/", headers=headers)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert HeaderKeys.request_id in response.headers
    assert response.headers.get(HeaderKeys.request_id) != dummy_request_id

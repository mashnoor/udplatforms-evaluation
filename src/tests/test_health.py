import pytest

from main import app


@pytest.fixture
async def test_hello(aiohttp_client, loop):
    client = await aiohttp_client(app)
    resp = await client.get('/')
    assert resp.status == 200

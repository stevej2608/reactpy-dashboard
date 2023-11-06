from fastapi import FastAPI
from httpx import AsyncClient
import pytest


@pytest.mark.anyio
async def xtest_hello(app: FastAPI, async_client: AsyncClient):
    response = await async_client.get('/')
    assert response


    

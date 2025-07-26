import pytest
from praktikum.bun import Bun


@pytest.fixture()
def create_bun():
    def create_bun(name='Булочка с корицей', price=85):
        return Bun(name=name, price=price)
    return create_bun

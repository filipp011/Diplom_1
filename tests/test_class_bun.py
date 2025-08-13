import pytest


class TestBun:

    @pytest.mark.parametrize("name", [
        "Булочка сладкаяя"
        "Булка с вареньем"
        "Сладкая булочка с корицей"
        "Булочка пустышка",

    ])
    def test_get_name_bun(self, name, create_bun):
        bun = create_bun(name=name)
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", [
        150.00,
        0.250,
        145.12
    ])
    def test_get_price_bun(self, price, create_bun):
        bun = create_bun(price=price)
        assert bun.get_price() == price
from praktikum.ingredient import Ingredient
import praktikum.ingredient_types
import pytest


class TestIngredients:
    @pytest.mark.parametrize("sauce_price, expected_price", [
    (200, 200),
    (150, 150),
    (300, 300),
])
    def test_get_price(self, sauce_price, expected_price):
        ingredient = Ingredient(
            praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE,
            "кисло-сладкий",
            sauce_price,
        )
        assert ingredient.get_price() == expected_price

    @pytest.mark.parametrize("sauce_name, expected_name", [
        ("кислый", "кислый"),
        ("острый", "острый"),
        ("чесночный", "чесночный"),
    ])
    def test_get_name(self, sauce_name, expected_name):
            ingredient = Ingredient(
                praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE, sauce_name, 200
            )
            assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize(
            "ingredient_type, name, price",
            [
                ("Котлета из говяжьих мозгов", "Семена", 1500),
                ("Адыгейский сыр", "Плавленый сыр с огнем", 412),
            ],
        )
    def test_get_type(self, ingredient_type, name, price):
            bun = Ingredient(ingredient_type, name, price)
            assert bun.get_type() == ingredient_type

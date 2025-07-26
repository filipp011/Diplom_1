from unittest.mock import Mock
import pytest
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
import praktikum.ingredient_types


class TestBurger:

    def test_burger_init(self):
        # Тестируем инициализацию класса Burger
        burger = Burger()
        # Проверяем, что у бургера нет булки и список ингредиентов пуст
        assert burger.bun is None and burger.ingredients == []

    @pytest.mark.parametrize('bun_name', ['Кисло-атомная булка', 'Нереальная булка'])
    def test_set_buns(self, bun_name):
        # Тестируем установку булки для бургера с разными названиями булок
        burger = Burger()
        # Проверяем, что булка установлена корректно
        assert burger.bun == burger.set_buns(bun_name)

    @pytest.mark.parametrize('ingredient', ['Остро-взырвной соус халапенью', 'Котлета баранья'])
    def test_add_ingredient(self, ingredient):
        # Тестируем добавление ингредиентов в бургер
        burger = Burger()
        burger.add_ingredient(ingredient)
        # Проверяем, что ингредиент добавлен в список ингредиентов бургера
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        # Тестируем удаление ингредиента из бургера
        ingredient = Ingredient(
            praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE, 'тестовый', 111.11)
        burger = Burger()
        burger.add_ingredient(ingredient)
        ingredients = burger.ingredients
        # Удаляем ингредиент по индексу 0
        burger.remove_ingredient(0)
        # Проверяем, что список ингредиентов теперь пуст
        assert ingredients == []

    def test_move_ingredient(self):
        # Тестируем перемещение ингредиента в списке ингредиентов бургера
        ingredient = Ingredient(
            praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE, 'тестовый', 111.11)
        another_ingredient = Ingredient(
            praktikum.ingredient_types.INGREDIENT_TYPE_FILLING, 'омлет', 200.10)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.add_ingredient(another_ingredient)
        # Перемещаем ингредиент с индекса 0 на индекс 1
        burger.move_ingredient(0, 1)
        # Проверяем, что порядок ингредиентов изменился
        assert burger.ingredients == [another_ingredient, ingredient]

    def test_get_price(self):
        # Тестируем расчет общей стоимости бургера
        bun_mock = Mock()
        ingredient_mock = Mock()
        bun_mock.get_price.return_value = 200  # Мокаем цену для булки
        ingredient_mock.get_price.return_value = 100  # Мокаем цену для ингредиента
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        # Проверяем, что общая стоимость рассчитана корректно
        assert burger.get_price() == 500  # 200 (булка) + 100 (ингредиент) + 200 (булка)

    def test_get_receipt(self):
        # Тестируем генерацию чека для бургера
        bun_mock = Mock()
        ingredient_mock = Mock()

        bun_mock.get_name.return_value = 'Вкусная'  # Мокаем название для булки
        bun_mock.get_price.return_value = 600.0  # Мокаем цену для булки
        ingredient_mock.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
        ingredient_mock.get_name.return_value = 'тестовый'  # Мокаем название для ингредиента
        ingredient_mock.get_price.return_value = 111.11  # Мокаем цену для ингредиента

        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)

        # Ожидаемый формат чека
        new_receipt = [
            '(==== Вкусная ====)',
            '= sauce тестовый =',
            '(==== Вкусная ====)\n',
            'Price: 1311.11'  # Расчет общей стоимости: 600 * 2 + 111.11
        ]

        # Проверяем, что сгенерированный чек соответствует ожидаемому формату
        assert burger.get_receipt() == '\n'.join(new_receipt)

            
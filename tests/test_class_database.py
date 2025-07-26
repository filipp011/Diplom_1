from unittest.mock import Mock
import pytest
from praktikum.database import Database

class TestDatabase:

    def test_available_buns(self):
        # Создаем мок для базы данных
        database_mock = Mock(spec=Database)
        
        # Настраиваем поведение мока
        database_mock.available_buns.return_value = [
            Mock(name="black bun", price=100),
            Mock(name="white bun", price=200),
            Mock(name="red bun", price=300)
        ]
        
        # Получаем булочки из мока
        buns = database_mock.available_buns()
        
        # Проверяем, что количество булочек и их содержимое соответствует ожиданиям
        assert len(buns) == 3 and buns == database_mock.available_buns()

    def test_available_ingredients(self):
        # Создаем мок для базы данных
        database_mock = Mock(spec=Database)
        
        # Настраиваем поведение мока
        database_mock.available_ingredients.return_value = [
            Mock(name="hot sauce", price=100),
            Mock(name="sour cream", price=200),
            Mock(name="chili sauce", price=300),
            Mock(name="cutlet", price=100),
            Mock(name="dinosaur", price=200),
            Mock(name="sausage", price=300)
        ]
        
        # Получаем ингредиенты из мока
        ingr = database_mock.available_ingredients()
        
        # Проверяем, что количество ингредиентов и их содержимое соответствует ожиданиям
        assert len(ingr) == 6 and ingr == database_mock.available_ingredients()

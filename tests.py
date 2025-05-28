import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize("book_name",
        ["",  # Пустая строка
        "a" * 41,  # Слишком длинная строка
        "a" * 40  # Граничная длина
        ])
    def test_add_new_book_invalid_length(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_add_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Гарри Поттер')
        assert len(collector.books_genre) == 1

    # Тесты для set_book_genre
    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        collector.set_book_genre('Матрица', 'Фантастика')
        assert collector.books_genre['Матрица'] == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        collector.set_book_genre('Матрица', 'Фэнтези')
        assert collector.books_genre['Матрица'] == ''

    # Тесты для get_books_for_children
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Шрек')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_for_children() == ['Шрек', 'Гарри Поттер']

    # Тесты для add_book_in_favorites
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        assert 'Властелин колец' in collector.favorites

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        assert collector.favorites.count('Властелин колец') == 1

    # Тесты для delete_book_from_favorites
    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')
        assert 'Властелин колец' not in collector.favorites

    # Тесты для get_books_with_specific_genre
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Матрица', 'Фантастика')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Матрица', 'Гарри Поттер']

    # Тесты для get_book_genre
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        collector.set_book_genre('Матрица', 'Фантастика')
        assert collector.get_book_genre('Матрица') == 'Фантастика'

    # Тесты для get_books_genre
    def test_get_books_genre(self, collector):
        collector.add_new_book('Матрица')
        collector.add_new_book('Гарри Поттер')
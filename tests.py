from main import BooksCollector
import pytest


class TestBooksCollector:

    # тесты для add_new_book 
    def test_add_new_book_creates_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert collector.get_book_genre('Гарри Поттер') == ''

    @pytest.mark.parametrize('name', ['', 'Очень длинное название книги, которое точно превышает сорок символов и не должно добавиться'])
    def test_add_new_book_invalid_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_duplicate_not_added_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    # тесты для set_book_genre
    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_set_book_genre_for_missing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Комедии')
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Научная фантастика')
        assert collector.get_book_genre('Книга') == ''

    # тесты для get_book_genre
    def test_get_book_genre_returns_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_book_genre_returns_none_for_missing_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая') is None

    # тесты для get_books_with_specific_genre 
    def test_get_books_with_specific_genre_returns_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер', 'Властелин колец']

    def test_get_books_with_specific_genre_empty_when_no_books(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_with_specific_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Детективы')
        assert collector.get_books_with_specific_genre('Научпоп') == []

    # тесты для get_books_genre
    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Комедии')
        assert collector.get_books_genre() == {'Книга': 'Комедии'}

    # тесты для get_books_for_children
    def test_get_books_for_children_only_child_friendly(self):
        collector = BooksCollector()
        collector.add_new_book('Король Лев')
        collector.set_book_genre('Король Лев', 'Мультфильмы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.add_new_book('Маска')
        collector.set_book_genre('Маска', 'Комедии')
        assert collector.get_books_for_children() == ['Король Лев', 'Маска']

    def test_get_books_for_children_empty_when_only_adult(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_for_children() == []

    # тесты для add_book_in_favorites 
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert collector.get_list_of_favorites_books() == ['Книга']

    def test_add_book_in_favorites_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_missing_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая')
        assert collector.get_list_of_favorites_books() == []

    # тесты для delete_book_from_favorites
    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_not_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.delete_book_from_favorites('Другая')
        assert collector.get_list_of_favorites_books() == []

    # тесты для get_list_of_favorites_books
    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_with_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга2')
        assert collector.get_list_of_favorites_books() == ['Книга1', 'Книга2']
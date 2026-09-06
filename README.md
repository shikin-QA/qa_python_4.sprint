# Проект BooksCollector — модульные тесты


### Метод add_new_book
test_add_new_book_creates_empty_genre — проверка, что после добавления книги её жанр — пустая строка
test_add_new_book_invalid_name_length — параметризованный тест: пустая строка и строка длиннее 40 символов не добавляются
test_add_new_book_duplicate_not_added_twice — одну и ту же книгу нельзя добавить дважды

### Метод set_book_genre
test_set_book_genre_success — корректная установка жанра существующей книге
test_set_book_genre_for_missing_book — попытка установить жанр отсутствующей книге не приводит к её появлению
test_set_book_genre_invalid_genre — недопустимый жанр не сохраняется

### Метод get_book_genre
test_get_book_genre_returns_genre — возвращает жанр существующей книги
test_get_book_genre_returns_none_for_missing_book — для несуществующей книги возвращает None

### Метод get_books_with_specific_genre
test_get_books_with_specific_genre_returns_books — выводит список книг с заданным жанром
test_get_books_with_specific_genre_empty_when_no_books — для жанра при пустой коллекции возвращается пустой список
test_get_books_with_specific_genre_invalid_genre — для недопустимого жанра возвращается пустой список

### Метод get_books_genre
test_get_books_genre_returns_dict — возвращает актуальный словарь книг и жанров

### Метод get_books_for_children
test_get_books_for_children_only_child_friendly — отбираются только книги с жанрами без возрастного рейтинга
test_get_books_for_children_empty_when_only_adult — если все книги с возрастным рейтингом, список пуст

### Метод add_book_in_favorites
test_add_book_in_favorites_success — успешное добавление существующей книги в избранное
test_add_book_in_favorites_duplicate_not_added — повторное добавление не дублирует книгу
test_add_book_in_favorites_missing_book — книга, которой нет в коллекции, не добавляется

### Метод delete_book_from_favorites
test_delete_book_from_favorites_success — удаление книги из избранного
test_delete_book_from_favorites_not_in_list — попытка удалить несуществующую книгу не вызывает ошибок

### Метод get_list_of_favorites_books
test_get_list_of_favorites_books_empty — возвращает пустой список, если избранных книг нет
test_get_list_of_favorites_books_with_books — возвращает список добавленных в избранное книг
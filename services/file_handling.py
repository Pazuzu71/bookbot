BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    page_text = text[start:(start + size)]

    while True:
        if page_text[-3] in ',.!:;?' and page_text[-2::] == '..':
            real_page_size = len(page_text)
            break
        elif page_text[-1] in ',.!:;?' and page_text[-2] in ',.!:;?' and page_text[-3] not in ',.!:;?':
            page_text = page_text[:-2]
        elif page_text[-1] in ',.!:;?' and page_text[-2] not in ',.!:;?':
            real_page_size = len(page_text)
            break
        else:
            page_text = page_text[:-1]

    return (page_text, real_page_size)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    pass


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)

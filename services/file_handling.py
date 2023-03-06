BOOK_PATH = 'book.txt'
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
    start = 0
    with open(path, encoding='UTF8') as f:
        text = f.read()
    size = PAGE_SIZE
    i = 1
    while len(text[start:]) > 0:
        page_text, real_page_size = _get_part_text(text, start, size)
        book[i] = page_text.strip()
        # print(i, book[i])
        i += 1
        start += real_page_size

    # print(book)


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)

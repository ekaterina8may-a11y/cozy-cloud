# TODO Найдите количество книг, которые можно скопировать на дискету

volume = 1.44 * 1024 * 1024  # объем в байтах
pages = 100
symbol_size = 4
line = 50
symbol = 25

book_size = pages * line * symbol * symbol_size
count = int (volume // book_size)

print("Количество книг, помещающихся на дискету:", count)

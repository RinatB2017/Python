# Импортируем библиотеку, соответствующую типу нашей базы данных 
import sqlite3

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
conn = sqlite3.connect('db/Chinook_Sqlite.sqlite')

# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

# ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
# КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ В ЭТО МЕСТО

# Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

# Получаем результат сделанного запроса
results = cursor.fetchall()
results2 =  cursor.fetchall()

print(results)   # [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]
print(results2)  # []

# Не забываем закрыть соединение с базой данных
conn.close()

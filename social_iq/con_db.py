import sqlite3
import pandas as pd

# Загрузка данных из CSV-файла
csv_file = 'research_iq.csv'
data = pd.read_csv(csv_file, delimiter=';')

# Преобразуем названия колонок в нижний регистр и заменим пробелы на подчеркивания
data.columns = [col.lower().replace(' ', '_') for col in data.columns]

# Подключение к базе данных SQLite (или создание базы данных, если она не существует)
conn = sqlite3.connect('instance/test.db')
cursor = conn.cursor()


# Подтверждение изменений и закрытие соединения
conn.commit()
conn.close()

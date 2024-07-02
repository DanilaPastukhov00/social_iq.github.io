import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Подключение к базе данных SQLite
conn = sqlite3.connect('instance/test.db')

# Чтение данных из таблицы в DataFrame
df = pd.read_sql_query('SELECT * FROM article;', conn)

# Закрытие соединения
conn.close()

# Set the style for the plots
sns.set(style="whitegrid")

# 1. Распределение по полу
open('static/img/gender_age_distribution.png', 'w+')
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.countplot(x='gender', data=df, palette='pastel')
plt.title('Распределение по полу')
plt.xlabel('Пол')
plt.ylabel('Количество')
plt.tight_layout()

# 2. Распределение по возрасту
plt.subplot(1, 2, 2)
sns.histplot(df['age'], bins=10, kde=True, color='skyblue')
plt.title('Распределение по возрасту')
plt.xlabel('Возраст')
plt.ylabel('Количество')
plt.tight_layout()
plt.savefig(f'static/img/gender_age_distribution.png')

# 3. Создание и сохранение круговых диаграмм для каждого вопроса
open(f'static/img/question_pie_chart.png', 'w+')

name_question = {1: ['Как Вы относитесь к технологиям искусственного интеллекта (ИИ) в целом?', 'Положительно',
                     'Отрицательно', 'Нейтрально'],
                 2: ['Какие нейронные сети Вы знаете?', 'Текстовые', 'Картинные', 'Знаю и текстовые, и картинные',
                     'Не знаю ни тех, ни других'],
                 3: ['Используете ли Вы в повседневной жизни текстовые нейросети?', 'Да', 'Нет'],
                 4: ['Для чего Вы чаще всего используете текстовые нейросети?', 'Решение практических задач',
                     'Развлечения', 'Трудно сказать'],
                 5: ['Используете ли Вы в повседневной жизни картинные нейросети?', 'Да', 'Нет'],
                 6: ['Для чего Вы чаще всего используете картиночные нейросети?', 'Решение практических задач',
                     'Развлечения', 'Трудно сказать'],
                 7: ['Помогают ли вам нейронные сети в решении повседневных задач?', 'Да', 'Нет',
                     'Затрудняюсь ответить'],
                 8: ['Верите ли Вы, что искусственный интеллект способен заменить человека?', 'Да', 'Нет',
                     'Затрудняюсь ответить'],
                 9: ['Что Вы думаете о применении искусственного интеллекта в различных сферах жизни?',
                     'ИИ должен использоваться во всех возможных сферах',
                     'ИИ следует использовать только в некоторых сферах',
                     'ИИ не должен использоваться вообще',
                     'Затрудняюсь ответить']}

plt.figure(figsize=(14, 15))

# через словарь прописать названия, добавить легенду ответов если нет идей то через html
for i in range(1, 10):
    question = f'question_{i}'
    responses = df[question].value_counts()
    total = df[question].count()
    labels = [f"{n} ({v / total:.1%})" for n, v in zip(name_question[i][1:], responses)]

    plt.subplot(5, 2, i)
    plt.pie(responses, colors=plt.cm.Paired.colors)
    plt.title(name_question[i][0])
    plt.legend(
        loc='center', bbox_to_anchor=(0, 0.1), labels=labels)
plt.tight_layout()
plt.savefig(f'static/img/question_pie_chart.png')

# 5. Средние значения по категориям
open('static/img/category_means.png', 'w+')

categories = {
    'self_awareness': [f'self_awareness_{i}' for i in range(1, 7)],
    'self_regulation': [f'self_regulation_{i}' for i in range(1, 7)],
    'empathy': [f'empathy_{i}' for i in range(1, 7)],
    'interaction_skills': [f'interaction_skills_{i}' for i in range(1, 6)],
    'self_motivation': [f'self_motivation_{i}' for i in range(1, 7)]
}

category_means = {cat: df[cols].mean().mean() * 100 for cat, cols in categories.items()}

plt.figure(figsize=(12, 6))
plt.bar(category_means.keys(), category_means.values(), color='lightgreen')
plt.title('% ответов по категориям')
plt.xlabel('Категория')
plt.ylabel('Среднее значение')
plt.savefig('static/img/category_means.png')

# Создание карты результатов
open('static/img/map_iq.png', 'w+')

generation = {
    'self_awareness': (df[[f'self_awareness_{i}' for i in range(1, 7)]].sum().sum()/6)/5,
    'self_regulation': (df[[f'self_regulation_{i}' for i in range(1, 7)]].sum().sum()/6)/5,
    'empathy': (df[[f'empathy_{i}' for i in range(1, 7)]].sum().sum()/6)/5,
    'interaction_skills': (df[[f'interaction_skills_{i}' for i in range(1, 7)]].sum().sum()/6)/5,
    'self_motivation': (df[[f'self_motivation_{i}' for i in range(1, 7)]].sum().sum()/6)/5
}

generation_z = df.query('age >= 1995 & age <= 2010')
generation_z_sums = {
    'self_awareness': (generation_z[[f'self_awareness_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_regulation': (generation_z[[f'self_regulation_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'empathy': (generation_z[[f'empathy_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'interaction_skills': (generation_z[[f'interaction_skills_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_motivation': (generation_z[[f'self_motivation_{i}' for i in range(1, 7)]].sum().sum()/5)/2
}

generation_y = df.query('age >= 1980 & age <= 1994')
generation_y_sums = {
    'self_awareness': (generation_y[[f'self_awareness_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_regulation': (generation_y[[f'self_regulation_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'empathy': (generation_y[[f'empathy_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'interaction_skills': (generation_y[[f'interaction_skills_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_motivation': (generation_y[[f'self_motivation_{i}' for i in range(1, 7)]].sum().sum()/5)/2
}

generation_x = df.query('age >= 1964 & age <= 1979')
generation_x_sums = {
    'self_awareness': (generation_x[[f'self_awareness_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_regulation': (generation_x[[f'self_regulation_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'empathy': (generation_x[[f'empathy_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'interaction_skills': (generation_x[[f'interaction_skills_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_motivation': (generation_x[[f'self_motivation_{i}' for i in range(1, 7)]].sum().sum()/5)/2
}

# man
generation_man = df.query('gender == "Мужской"')
generation_sums_man = {
    'self_awareness': (generation_z[[f'self_awareness_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_regulation': (generation_z[[f'self_regulation_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'empathy': (generation_z[[f'empathy_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'interaction_skills': (generation_z[[f'interaction_skills_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_motivation': (generation_z[[f'self_motivation_{i}' for i in range(1, 7)]].sum().sum()/5)/2
}

generation_z_man = df.query('age >= 1995 & age <= 2010 & gender == "Мужской"')
generation_z_sums_man = {
    'self_awareness': (generation_z[[f'self_awareness_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_regulation': (generation_z[[f'self_regulation_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'empathy': (generation_z[[f'empathy_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'interaction_skills': (generation_z[[f'interaction_skills_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_motivation': (generation_z[[f'self_motivation_{i}' for i in range(1, 7)]].sum().sum()/5)/2
}

generation_y_man = df.query('age >= 1980 & age <= 1994 & gender == "Мужской"')
generation_y_sums_man = {
    'self_awareness': (generation_y[[f'self_awareness_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_regulation': (generation_y[[f'self_regulation_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'empathy': (generation_y[[f'empathy_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'interaction_skills': (generation_y[[f'interaction_skills_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_motivation': (generation_y[[f'self_motivation_{i}' for i in range(1, 7)]].sum().sum()/5)/2
}

generation_x_man = df.query('age >= 1964 & age <= 1979 & gender == "Мужской"')
generation_x_sums_man = {
    'self_awareness': (generation_x[[f'self_awareness_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_regulation': (generation_x[[f'self_regulation_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'empathy': (generation_x[[f'empathy_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'interaction_skills': (generation_x[[f'interaction_skills_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_motivation': (generation_x[[f'self_motivation_{i}' for i in range(1, 7)]].sum().sum()/5)/2
}

# woman
generation_woman = df.query('gender == "Женский"')
generation_sums_woman = {
    'self_awareness': (generation_z[[f'self_awareness_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_regulation': (generation_z[[f'self_regulation_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'empathy': (generation_z[[f'empathy_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'interaction_skills': (generation_z[[f'interaction_skills_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_motivation': (generation_z[[f'self_motivation_{i}' for i in range(1, 7)]].sum().sum()/5)/2
}

generation_z_woman = df.query('age >= 1995 & age <= 2010 & gender == "Женский"')
generation_z_sums_woman = {
    'self_awareness': (generation_z[[f'self_awareness_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_regulation': (generation_z[[f'self_regulation_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'empathy': (generation_z[[f'empathy_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'interaction_skills': (generation_z[[f'interaction_skills_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_motivation': (generation_z[[f'self_motivation_{i}' for i in range(1, 7)]].sum().sum()/5)/2
}

generation_y_woman = df.query('age >= 1980 & age <= 1994 & gender == "Женский"')
generation_y_sums_woman = {
    'self_awareness': (generation_y[[f'self_awareness_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_regulation': (generation_y[[f'self_regulation_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'empathy': (generation_y[[f'empathy_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'interaction_skills': (generation_y[[f'interaction_skills_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_motivation': (generation_y[[f'self_motivation_{i}' for i in range(1, 7)]].sum().sum()/5)/2
}

generation_x_woman = df.query('age >= 1964 & age <= 1979 & gender == "Женский"')
generation_x_sums_woman = {
    'self_awareness': (generation_x[[f'self_awareness_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_regulation': (generation_x[[f'self_regulation_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'empathy': (generation_x[[f'empathy_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'interaction_skills': (generation_x[[f'interaction_skills_{i}' for i in range(1, 7)]].sum().sum()/5)/2,
    'self_motivation': (generation_x[[f'self_motivation_{i}' for i in range(1, 7)]].sum().sum()/5)/2
}

plt.figure(figsize=(14, 15))

map_iq = [generation, generation_z_sums, generation_y_sums, generation_x_sums,
          generation_sums_man, generation_z_sums_man, generation_y_sums_man, generation_x_sums_man,
          generation_sums_woman, generation_z_sums_woman, generation_y_sums_woman, generation_x_sums_woman]
index = list(range(1, 13))
title = ['Общее', 'Поколение Z', 'Поколение Y', 'Поколение X',
         'Общее значение для мужчин', 'Мужчины поколения Z', 'Мужчины поколения Y', 'Мужчины поколения X',
         'Общее значение для женщин', 'Женщины поколения Z', 'Женщины поколения Y', 'Женщины поколения X']

for h, c, x in zip(index, map_iq, title):
    plt.subplot(6, 2, h)
    plt.bar(c.keys(), c.values(), color='skyblue')
    plt.title(x)
plt.tight_layout()
plt.savefig('static/img/map_iq.png')


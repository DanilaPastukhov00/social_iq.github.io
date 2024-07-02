import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import statistics
# from sklearn.metrics import r2_score, mean_squared_error


# Подключение к базе данных SQLite
conn = sqlite3.connect('instance/test.db')

# Чтение данных из таблицы в DataFrame
research = pd.read_sql_query('SELECT * FROM article;', conn)

# Закрытие соединения
conn.close()


research['self_awareness'] = research['self_awareness_1'] + research['self_awareness_2'] + research[
    'self_awareness_3'] + research['self_awareness_4'] + research['self_awareness_5'] + research['self_awareness_6']

research['self_regulation'] = research['self_regulation_1'] + research['self_regulation_2'] + research[
    'self_regulation_3'] + research['self_regulation_4'] + research['self_regulation_5'] + research[
    'self_regulation_6']

research['empathy'] = research['empathy_1'] + research['empathy_2'] + research['empathy_3'] + research[
    'empathy_4'] + research['empathy_5'] + research['empathy_6']

research['interaction_skills'] = research['interaction_skills_1'] + research['interaction_skills_2'] + research[
    'interaction_skills_3'] + research['interaction_skills_4'] + research['interaction_skills_5'] + research[
    'interaction_skills_6']

research['self_motivation'] = research['self_motivation_1'] + research['self_motivation_2'] + research[
    'self_motivation_3'] + research['self_motivation_4'] + research['self_motivation_5'] + research[
    'self_motivation_6']

research['gender'] = research['gender'].map({'Мужской': 0, 'Женский': 1})
feature = ['gender', 'age', 'question_1', 'question_2', 'question_3', 'question_4',
           'question_5', 'question_6', 'question_7', 'question_8', 'question_9', 'self_motivation',
           'empathy', 'interaction_skills', 'self_regulation', 'self_awareness']


def predict_iq():
    # Случайный лес
    x = research[feature]
    y = research[feature[11:]]

    # разделение набора данных на тестовую и обучающую выборку
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=22)

    # self_motivation
    self_motivation = RandomForestRegressor(n_estimators=1000, bootstrap=True, random_state=1)
    self_motivation.fit(x_train[feature[:-5]], y_train['self_motivation'])

    # empathy
    empathy = RandomForestRegressor(n_estimators=1000, bootstrap=True, random_state=1)
    empathy.fit(x_train[feature[:-4]], y_train['empathy'])

    # interaction_skills
    interaction_skills = RandomForestRegressor(n_estimators=1000, bootstrap=True, random_state=1)
    interaction_skills.fit(x_train[feature[:-3]], y_train['interaction_skills'])

    # self_regulation
    self_regulation = RandomForestRegressor(n_estimators=1000, bootstrap=True, random_state=1)
    self_regulation.fit(x_train[feature[:-2]], y_train['self_regulation'])

    # self_awareness
    self_awareness = RandomForestRegressor(n_estimators=1000, bootstrap=True, random_state=1, min_samples_leaf=5)
    self_awareness.fit(x_train[feature[:-1]], y_train['self_awareness'])

    # Совмещение
    n = x_test[feature[:-5]].reset_index(drop=True)

    n_1 = pd.concat([n, pd.DataFrame(self_motivation.predict(n), columns=['self_motivation'])], axis=1)

    n_2 = pd.concat([n_1, pd.DataFrame(empathy.predict(n_1), columns=['empathy'])], axis=1)

    n_3 = pd.concat([n_2, pd.DataFrame(interaction_skills.predict(n_2), columns=['interaction_skills'])], axis=1)

    n_4 = pd.concat([n_3, pd.DataFrame(self_regulation.predict(n_3), columns=['self_regulation'])], axis=1)

    predict = pd.concat([n_4, pd.DataFrame((self_awareness.predict(n_4)), columns=['self_awareness'])], axis=1)

    # Результаты исследования
    avg_self_motivation = statistics.mean(predict['self_motivation'])
    avg_empathy = statistics.mean(predict['empathy'])
    avg_interaction_skills = statistics.mean(predict['interaction_skills'])
    avg_self_regulation = statistics.mean(predict['self_regulation'])
    avg_self_awareness = statistics.mean(predict['self_awareness'])
    overall_avg_result = statistics.mean([avg_self_awareness, avg_self_regulation, avg_empathy,
                                         avg_interaction_skills, avg_self_motivation])

    return {'self_motivation': avg_self_motivation,
            'empathy': avg_empathy,
            'interaction_skills': avg_interaction_skills,
            'self_regulation': avg_self_regulation,
            'self_awareness': avg_self_awareness,
            'overall_result': overall_avg_result}


def tests():
    tests_self_motivation = statistics.mean(research['self_motivation'])
    tests_empathy = statistics.mean(research['empathy'])
    tests_interaction_skills = statistics.mean(research['interaction_skills'])
    tests_self_regulation = statistics.mean(research['self_regulation'])
    tests_self_awareness = statistics.mean(research['self_awareness'])
    overall_tests_result = statistics.mean([tests_self_motivation, tests_empathy, tests_interaction_skills,
                                            tests_self_regulation, tests_self_awareness])

    return {'self_motivation': tests_self_motivation,
            'empathy': tests_empathy,
            'interaction_skills': tests_interaction_skills,
            'self_regulation': tests_self_regulation,
            'self_awareness': tests_self_awareness,
            'overall_result': overall_tests_result}


# print(f"elf_motivation {avg_self_motivation}\nempathy {avg_empathy}\ninteraction_skills {avg_interaction_skills}")
# print(f"self_regulation {avg_self_regulation}\nself_awareness {avg_self_awareness}")
# print(f'Общая оценка: {overall_avg_result}')
#
# # Итог соотношения метрик
# print('self-motivation')
# print('mean_squared_error: ', mean_squared_error(y_test['self-motivation'], avg_self_motivation))
# print('r2_score: ', r2_score(y_test['self-motivation'], avg_self_motivation))
# print('empathy')
# print('mean_squared_error: ', mean_squared_error(y_test['empathy'], avg_empathy))
# print('r2_score: ', r2_score(y_test['empathy'], avg_empathy))
# print('interaction_skills')
# print('mean_squared_error: ', mean_squared_error(y_test['interaction_skills'], avg_interaction_skills))
# print('r2_score: ', r2_score(y_test['interaction_skills'], avg_interaction_skills))
# print('self-regulation')
# print('mean_squared_error: ', mean_squared_error(y_test['self-regulation'], avg_self_regulation))
# print('r2_score: ', r2_score(y_test['self-regulation'], avg_self_regulation))
# print('self-awareness')
# print('mean_squared_error: ', mean_squared_error(y_test['self-awareness'], overall_avg_result))
# print('r2_score: ', r2_score(y_test['self-awareness'], overall_avg_result))

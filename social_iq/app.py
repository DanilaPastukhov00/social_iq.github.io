from flask import Flask, render_template, send_from_directory, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
import predict_social_iq

os.system('python research.py')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    question_1 = db.Column(db.Text, nullable=False)
    question_2 = db.Column(db.Text, nullable=False)
    question_3 = db.Column(db.Text, nullable=False)
    question_4 = db.Column(db.Text, nullable=False)
    question_5 = db.Column(db.Text, nullable=False)
    question_6 = db.Column(db.Text, nullable=False)
    question_7 = db.Column(db.Text, nullable=False)
    question_8 = db.Column(db.Text, nullable=False)
    question_9 = db.Column(db.Text, nullable=False)
    self_awareness_1 = db.Column(db.Integer, nullable=True, default=0)
    self_awareness_2 = db.Column(db.Integer, nullable=True, default=0)
    self_awareness_3 = db.Column(db.Integer, nullable=True, default=0)
    self_awareness_4 = db.Column(db.Integer, nullable=True, default=0)
    self_awareness_5 = db.Column(db.Integer, nullable=True, default=0)
    self_awareness_6 = db.Column(db.Integer, nullable=True, default=0)
    self_regulation_1 = db.Column(db.Integer, nullable=True, default=0)
    self_regulation_2 = db.Column(db.Integer, nullable=True, default=0)
    self_regulation_3 = db.Column(db.Integer, nullable=True, default=0)
    self_regulation_4 = db.Column(db.Integer, nullable=True, default=0)
    self_regulation_5 = db.Column(db.Integer, nullable=True, default=0)
    self_regulation_6 = db.Column(db.Integer, nullable=True, default=0)
    empathy_1 = db.Column(db.Integer, nullable=True, default=0)
    empathy_2 = db.Column(db.Integer, nullable=True, default=0)
    empathy_3 = db.Column(db.Integer, nullable=True, default=0)
    empathy_4 = db.Column(db.Integer, nullable=True, default=0)
    empathy_5 = db.Column(db.Integer, nullable=True, default=0)
    empathy_6 = db.Column(db.Integer, nullable=True, default=0)
    interaction_skills_1 = db.Column(db.Integer, nullable=True, default=0)
    interaction_skills_2 = db.Column(db.Integer, nullable=True, default=0)
    interaction_skills_3 = db.Column(db.Integer, nullable=True, default=0)
    interaction_skills_4 = db.Column(db.Integer, nullable=True, default=0)
    interaction_skills_5 = db.Column(db.Integer, nullable=True, default=0)
    interaction_skills_6 = db.Column(db.Integer, nullable=True, default=0)
    self_motivation_1 = db.Column(db.Integer, nullable=True, default=0)
    self_motivation_2 = db.Column(db.Integer, nullable=True, default=0)
    self_motivation_3 = db.Column(db.Integer, nullable=True, default=0)
    self_motivation_4 = db.Column(db.Integer, nullable=True, default=0)
    self_motivation_5 = db.Column(db.Integer, nullable=True, default=0)
    self_motivation_6 = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return 'Article %r' % self.id


@app.route('/')
def index():
    predict = predict_social_iq.predict_iq()
    tests = predict_social_iq.tests()
    return render_template('index.html', predict=predict, tests=tests)


@app.route('/text', methods=['POST', 'GET'])
def text():
    if request.method == "POST":
        gender = request.form['gender']
        age = request.form['age']
        question_1 = request.form['question_1']
        question_2 = request.form['question_2']
        question_3 = request.form['question_3']
        question_4 = request.form['question_4']
        question_5 = request.form['question_5']
        question_6 = request.form['question_6']
        question_7 = request.form['question_7']
        question_8 = request.form['question_8']
        question_9 = request.form['question_9']
        self_awareness_1 = request.form['self_awareness_1']
        self_awareness_2 = request.form['self_awareness_2']
        self_awareness_3 = request.form['self_awareness_3']
        self_awareness_4 = request.form['self_awareness_4']
        self_awareness_5 = request.form['self_awareness_5']
        self_awareness_6 = request.form['self_awareness_6']
        self_regulation_1 = request.form['self_regulation_1']
        self_regulation_2 = request.form['self_regulation_2']
        self_regulation_3 = request.form['self_regulation_3']
        self_regulation_4 = request.form['self_regulation_4']
        self_regulation_5 = request.form['self_regulation_5']
        self_regulation_6 = request.form['self_regulation_6']
        empathy_1 = request.form['empathy_1']
        empathy_2 = request.form['empathy_2']
        empathy_3 = request.form['empathy_3']
        empathy_4 = request.form['empathy_4']
        empathy_5 = request.form['empathy_5']
        empathy_6 = request.form['empathy_6']
        interaction_skills_1 = request.form['interaction_skills_1']
        interaction_skills_2 = request.form['interaction_skills_2']
        interaction_skills_3 = request.form['interaction_skills_3']
        interaction_skills_4 = request.form['interaction_skills_4']
        interaction_skills_5 = request.form['interaction_skills_5']
        interaction_skills_6 = request.form['interaction_skills_6']
        self_motivation_1 = request.form['self_motivation_1']
        self_motivation_2 = request.form['self_motivation_2']
        self_motivation_3 = request.form['self_motivation_3']
        self_motivation_4 = request.form['self_motivation_4']
        self_motivation_5 = request.form['self_motivation_5']
        self_motivation_6 = request.form['self_motivation_6']

        article = Article(gender=gender, age=age,
                          question_1=question_1,
                          question_2=question_2,
                          question_3=question_3,
                          question_4=question_4,
                          question_5=question_5,
                          question_6=question_6,
                          question_7=question_7,
                          question_8=question_8,
                          question_9=question_9,
                          self_awareness_1=self_awareness_1,
                          self_awareness_2=self_awareness_2,
                          self_awareness_3=self_awareness_3,
                          self_awareness_4=self_awareness_4,
                          self_awareness_5=self_awareness_5,
                          self_awareness_6=self_awareness_6,
                          self_regulation_1=self_regulation_1,
                          self_regulation_2=self_regulation_2,
                          self_regulation_3=self_regulation_3,
                          self_regulation_4=self_regulation_4,
                          self_regulation_5=self_regulation_5,
                          self_regulation_6=self_regulation_6,
                          empathy_1=empathy_1,
                          empathy_2=empathy_2,
                          empathy_3=empathy_3,
                          empathy_4=empathy_4,
                          empathy_5=empathy_5,
                          empathy_6=empathy_6,
                          interaction_skills_1=interaction_skills_1,
                          interaction_skills_2=interaction_skills_2,
                          interaction_skills_3=interaction_skills_3,
                          interaction_skills_4=interaction_skills_4,
                          interaction_skills_5=interaction_skills_5,
                          interaction_skills_6=interaction_skills_6,
                          self_motivation_1=self_motivation_1,
                          self_motivation_2=self_motivation_2,
                          self_motivation_3=self_motivation_3,
                          self_motivation_4=self_motivation_4,
                          self_motivation_5=self_motivation_5,
                          self_motivation_6=self_motivation_6)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return "ERROR"
    else:
        return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)

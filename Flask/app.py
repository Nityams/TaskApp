from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Task %r>' % self.id
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'date_created': self.date_created,
        }

@app.route('/add',methods=['POST'])
def add():
    task_content = json.loads(request.data.decode('utf8').replace("'", '"'))
    new_task = Todo(content=task_content["content"])
    try:
        db.session.add(new_task)
        db.session.commit()
        return "done"
    except:
        return "There was an issue adding your task"

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = json.loads(request.data.decode('utf8').replace("'", '"'))
        new_task = Todo(content=task_content["content"])
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            response = app.response_class(
            status=500,
            mimetype='application/json'
            )
            return e
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        response = app.response_class(
            response = jsonify(task_list=[i.serialize for i in tasks]),
            status = 200,
            mimetype='application/json'
        )
        return jsonify(task_list=[i.serialize for i in tasks])

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
            response = app.response_class(
            status=500,
            mimetype='application/json'
            )
            return e


@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task_to_update.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            response = app.response_class(
            status=500,
            mimetype='application/json'
            )
            return e
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        response = app.response_class(
            response = jsonify(task_list=[i.serialize for i in tasks]),
            status = 200,
            mimetype='application/json'
        )
        return jsonify(task_list=[i.serialize for i in tasks])


if __name__ == "__main__":
    app.run(debug=True)
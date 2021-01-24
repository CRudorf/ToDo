from app import app, db
from app.models import User, Todo


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Todo': Todo}


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

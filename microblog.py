from app import create_app, db
from app.models import User, Post, Message, Notification, Task

app = create_app()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post,
            'Message': Message, 'Notification': Notification,
            'Task': Task}

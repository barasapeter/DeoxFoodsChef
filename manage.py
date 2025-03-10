from flask_script import Manager
from app import create_app

app = create_app('development')
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
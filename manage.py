# -*- coding: utf-8 -*-

from app import create_myapp
from flask.ext.script import Manager

app = create_myapp()
manager = Manager(app)

if __name__ == '__main__':
	manager.run()
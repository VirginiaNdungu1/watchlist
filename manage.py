from app import create_app
from flask_script import Manager, Server

app = create_app('development')
'''
Create app instance
How?

Call the create_app function
pass in the onfiguration_options key - 'development'
'''

manager = Manager(app)
'''
Instantiate the Manager Class
How?
Pass in the app instance
'''

manager.add_command('server', Server)
'''
Create a new command 'server' to launch the application server
'''


@manager.command
def test():
    '''
    function to run the unittests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()

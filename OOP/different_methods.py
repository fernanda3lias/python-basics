# method vs @classmethod vs @staticmethod
# method - self, instance method
# @classmethod - cls, class method
# @staticmethod - static method (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('LOG: ', msg)

# connection_one = Connection()
# connection_one.set_user('Charles')
# connection_one.set_password('123')
        
connection_one = Connection.create_with_auth('Charles', '123')

print(connection_one.user)
print(connection_one.password)
print(Connection.log('This is the log message.'))

# Abstraction
# Inheritance - Is 
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, message):
        raise NotImplementedError(
            'Implement the log method'
        )
    
    def log_error(self, message):
        self._log(f'Error: {message}')

    def log_success(self, message):
        self._log(f'Success: {message}')
    
    
class LogFileMixin(Log):
    def _log(self, message):
        formated_message = f'{message} ({self.__class__.__name__})'
        print('Saving on log: ', formated_message)
        with open(LOG_FILE, 'w') as file:
            file.write(formated_message)
            file.write('\n')

class LogPrintMixin(Log):
    def _log(self, message):
        print(f'{message} ({self.__class__.__name__})')

if __name__ =='__main__':
    lp = LogPrintMixin()
    lp.log_error('Anything')
    lp.log_success('Cool')

    lf = LogFileMixin()
    lf.log_error('Anything')
    lf.log_success('Cool')
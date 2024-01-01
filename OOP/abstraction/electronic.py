from log import LogFileMixin

class Electronic:
    def __init__(self, name):
        self._name = name
        self._powered = False

    def turn_on(self):
        if not self._powered:
            self._powered = True

    def turn_off(self):
        if self._powered:
            self._powered = False


class Smartphone(Electronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()

        if self._powered:
            message = f'{self._name} is powered.'
            self.log_success(message)

    def turn_off(self):
        super().turn_off()

        if not self._powered:
            message = f'{self._name} is not powered.'
            self.log_error(message)
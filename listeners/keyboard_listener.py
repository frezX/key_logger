from logger import Logger
from pynput.keyboard import Listener


class KeyboardListener:
    def __init__(self):
        self.logger: Logger = Logger(logger_name='Keyboard')

    @staticmethod
    def _get_key_name(key) -> str:
        try:
            key_name: str = key.name
        except AttributeError:
            key_name: str = key.char
        return key_name

    def on_release(self, key) -> None:
        self.logger(
            text=f'{self._get_key_name(key=key)} release'
        )

    def on_press(self, key) -> None:
        self.logger(
            text=f'{self._get_key_name(key=key)} press'
        )

    def run(self) -> None:
        try:
            with Listener(on_press=self.on_press, on_release=self.on_release) as listener_:
                listener_.join()
        except Exception as e:
            self.logger(text=str(e), status='ERROR')

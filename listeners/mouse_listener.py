from logger import Logger
from pynput.mouse import Listener


class MouseListener:
    def __init__(self):
        self.logger: Logger = Logger(logger_name='Mouse')
        self.mouse_buttons: dict = {
            'left': 'Left button',
            'right': 'Right button',
            'middle': 'Middle button',
            'button8': 'Forward button',
            'button9': 'Backward button'
        }

    def on_click(self, _, __, button, pressed: bool) -> None:
        self.logger(
            text=f'{self.mouse_buttons.get(button.name, button.name)} {"press" if pressed else "release"}'
        )

    def run(self) -> None:
        try:
            with Listener(on_click=self.on_click) as listener_:
                listener_.join()
        except Exception as e:
            self.logger(text=str(e), status='ERROR')

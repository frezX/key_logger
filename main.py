from threading import Thread
from listeners import MouseListener, KeyboardListener


class Listener:
    def __init__(self):
        self.mouse_listener: MouseListener = MouseListener()
        self.keyboard_listener: KeyboardListener = KeyboardListener()

    def run(self) -> None:
        Thread(target=self.mouse_listener.run).start()
        Thread(target=self.keyboard_listener.run).start()


if __name__ == '__main__':
    listener: Listener = Listener()
    listener.run()

import os
import sys
from time import strftime


class Logger:
    def __init__(self, logger_name: str):
        self.logger_name: str = logger_name
        self.__dir: str = 'log'
        self.__make_dir(path=self.__dir)
        self.__path: str = f'{self.__dir}/{self.logger_name.lower()}_log.txt'
        self.print = lambda text: sys.stdout.write(f'{text}\n')

    @staticmethod
    def __make_dir(path: str) -> None:
        if not os.path.exists(path):
            os.mkdir(path)

    def write_in_log_file(self, log_text: str) -> None:
        with open(file=self.__path, mode='a+') as file:
            print(log_text, file=file)

    def __call__(self, text: str, status: str = 'INFO') -> None:
        log_text: str = f'{status} [{strftime("%X")}]: {text}'
        self.print(text=log_text)
        self.write_in_log_file(log_text=log_text)

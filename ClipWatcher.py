from threading import Thread
from time import sleep
from itertools import cycle

from pyperclip import paste

class ClipWatcher(Thread):
    def __init__(self, validater, callback, delay=.5):
        Thread.__init__(self)
        self.daemon = True
        self._validater = validater
        self._callback = callback
        self._delay = delay
        self._running = True

    def run(self):       
        recent_value = ''
        while self._running:
            tmp_value = paste()
            if tmp_value != recent_value:
                recent_value = tmp_value
                if self._validater(recent_value):
                    self._callback(recent_value)
            sleep(self._delay)

    def stop(self):
        self._running = False
        print('Thread State running:', self._running)

    def start(self):
        super().start()
        while self._running:
            for i in cycle('|/-\\'):
                sleep(0.1)
                yield i

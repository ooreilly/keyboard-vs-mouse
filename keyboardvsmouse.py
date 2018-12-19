"""
Keyboard vs Mouse client application
Use this application to connect to a keyboard vs mouse server and upload your
stats.

The first time you use this client you must edit `config.py`. Open this file
and follow the instructions there.

"""
import keyboard
from pynput import mouse
import time
import config as cfg
import stats
import client

cli = client.Client(cfg.host, cfg.login)
cli.authorize()

log = stats.Stats()

log.time = time.time()
log.startTime = time.time()

print('Start typing to collect points')
print('Press `q` to exit.')
print('As long as you leave this window open and do not drop your connection '\
      'you will collect points.')
print('Go ahead and do other tasks now.')

def on_release(e):
    log.recordKeyPress()
    log.recordTime(time.time())
    log.time = time.time()
    status = cli.submit(log.getData())
    if status:
        log.reset()
    print(log)

def on_move(x, y):
    log.recordMotion()
    log.recordTime(time.time())
    log.time = time.time()
    status = cli.submit(log.getData())
    if status:
        log.reset()
    print(log)
def on_click(x, y, button, pressed):
    log.recordButtonPress()
    log.recordTime(time.time())
    log.time = time.time()
    status = cli.submit(log.getData())
    if status:
        log.reset()
    print(log)

def on_scroll(x, y, dx, dy):
    pass

keyboard.on_release(on_release)

with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

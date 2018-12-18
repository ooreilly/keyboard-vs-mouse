"""
Keyboard vs Mouse client application
Use this application to connect to a keyboard vs mouse server and upload your
stats.

The first time you use this client you must edit `config.py`. Open this file
and follow the instructions there.

"""
from Xlib import X, XK, display
from Xlib.ext import record
from Xlib.protocol import rq
import time
import os
import sys
import config2 as cfg
import stats
import client

cli = client.Client(cfg.host, cfg.login)
cli.authorize()

session = display.Display()
log = stats.Stats()

log.time = time.time()
log.startTime = time.time()

print('Start typing to collect points')
print('Press `q` to exit.')
print('As long as you leave this window open and do not drop your connection '\
      'you will collect points.')
print('Go ahead and do other tasks now.')
 
def finalize(keysym):
    for name in dir(XK):
        if name[:3] == "XK_" and name[3:] == "q" and getattr(XK, name) == keysym:
            print("bye")
            exit(1)

def callback(reply):
    if not len(reply.data):
        return
    data = reply.data
    
    # Please don't mess with this to cheat. If I catch you cheating I will reset
    # your stats and come up with something very clever so that it will be
    # difficult for you to cheat again!
    while len(data):
        event, data = rq.EventField(None).parse_binary_value(data,
                session.display, None, None)
        finalize(session.keycode_to_keysym(event.detail, 0))
        if event.type == X.ButtonPress:
            log.recordButtonPress()
        if event.type == X.KeyRelease:
            log.recordKeyPress()
        if event.type == X.MotionNotify:
            log.recordMotion()

    print(log)
    log.recordTime(time.time())
    log.time = time.time()

    status = cli.submit(log.getData())
    if status:
        log.reset()

ctx = session.record_create_context(
        0,
        [record.AllClients],
        [{
                'core_requests': (0, 0),
                'core_replies': (0, 0),
                'ext_requests': (0, 0, 0, 0),
                'ext_replies': (0, 0, 0, 0),
                'delivered_events': (0, 0),
                'device_events': (X.KeyPress, X.EnterNotify, X.ButtonPress,
                                  X.KeyRelease),
                'errors': (0, 0),
                'client_started': False,
                'client_died': False,
        }])

session.record_enable_context(ctx, callback)
session.record_free_context(ctx)

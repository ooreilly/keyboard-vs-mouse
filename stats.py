
class Stats(object):

    def __init__(self):
        self.stats = {'keyPress': 0, 'buttonPress': 0, 'motion': 0,
                'activeTime': 0, 'idleTime': 0, 'time': 0}
        self.total = {key : self.stats[key] for key in self.stats}
        self.time = 0
        self.startTime = 0

    def recordButtonPress(self):
        self.stats['buttonPress'] += 1

    def recordKeyPress(self):
        self.stats['keyPress'] += 1

    def recordMotion(self):
        self.stats['motion'] += 1

    def recordTime(self, time):
        self.stats['time'] = time - self.time

    def getData(self):
        return self.stats

    def reset(self):
        self.total = {key : self.total[key] + self.stats[key] for key in
                      self.total}
        self.stats = {key : 0 for key in self.total}


    def __str__(self):
        return ("Key press: %d, Mouse motion: %d, Button press: %d, Time: %g" % 
                (self.stats['keyPress'], self.stats['motion'],
                self.stats['buttonPress'],
                self.stats['time']
                ))


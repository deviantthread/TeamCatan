import collections


class AuditLog:
    def __init__(self):
        log = collections.deque(maxlen=100)

    def append(self, msg):
        self.log.append(msg)

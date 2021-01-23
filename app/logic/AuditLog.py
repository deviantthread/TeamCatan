import collections


class AuditLog:
    def __init__(self):
        self.log = collections.deque(maxlen=100)

    def append(self, msg):
        self.log.append(msg)

    def as_list(self):
        return list(self.log)

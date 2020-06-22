class Passenger(object):
    """docstring for Passenger"""
    def __init__(self, idnum,arrivalTime):
        super(Passenger, self).__init__()
        self._idnum = idnum
        self._arrivalTime = arrivalTime

    def idNum(self):
        return self._idnum

    def arrivalTime(self):
        return self._arrivalTime

class TicketAgent(object):
    """docstring for TicketAgent"""
    def __init__(self,idnum):
        super(TicketAgent, self).__init__()
        self._passenger = None
        self._stoptime = -1
        self._idnum = idnum

    def idNum(self):
        return self._idnum

    def isFree(self):
        return self._passenger is None

    def isFinished(self,stopTime):
        return self._passenger is not None and self._stoptime== stopTime

    def startService(self,passenger,stopTime):
        self._passenger = passenger
        self._stoptime = stopTime

    def stopService(self):
        passenger = self._passenger
        self._passenger = None
        return passenger

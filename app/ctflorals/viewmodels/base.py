from ctflorals.models import Navigation

class BaseViewModel(object):

    def __init__(self):
        self.navigation = Navigation()

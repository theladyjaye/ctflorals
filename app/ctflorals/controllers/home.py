from .base import BaseController
from ctflorals.services import SimpleService

class HomeController(BaseController):
    def index(self):
        service = SimpleService()
        viewdata = service.home_viewdata()
        return self.view('home.html', viewdata)

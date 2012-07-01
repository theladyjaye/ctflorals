from .base import BaseController
from ctflorals.services import SimpleService

class AboutController(BaseController):
    def index(self):
        service = SimpleService()
        viewdata = service.about_viewdata()
        return self.view('about.html', viewdata)

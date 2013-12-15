from .base import BaseController
from ctflorals.services import SimpleService

class TestimonialsController(BaseController):
    def index(self):
        service = SimpleService()
        viewdata = service.testimonials_viewdata()
        return self.view('testimonials.html', viewdata)

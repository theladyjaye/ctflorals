from .base import BaseController
from ctflorals.services import SimpleService

class GalleryController(BaseController):
    def index(self):
        service = SimpleService()
        viewdata = service.gallery_viewdata()
        return self.view('gallery.html', viewdata)

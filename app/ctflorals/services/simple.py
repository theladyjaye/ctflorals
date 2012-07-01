from .base import BaseService
from ctflorals.viewmodels import BaseViewModel

class SimpleService(BaseService):

    def home_viewdata(self):
        model = BaseViewModel()
        model.navigation.home = "selected"
        return model

    def about_viewdata(self):
        model = BaseViewModel()
        model.navigation.about = "selected"
        return model

    def gallery_viewdata(self):
        model = BaseViewModel()
        model.navigation.gallery = "selected"
        return model

    def testimonials_viewdata(self):
        model = BaseViewModel()
        model.navigation.testimonials = "selected"
        return model

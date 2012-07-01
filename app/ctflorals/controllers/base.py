from flask import render_template
#from flask import make_response
class BaseController(object):

    def view(self, view, model=None):
        #response = make_response(render_template(view, model=model))
        #response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return render_template(view, model=model)


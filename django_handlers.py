# -*- coding: utf-8 -*-
import os
import datetime
import webapp2
from django import template

class BaseHandler(webapp2.RequestHandler):
    def render_template(self, template_name, template_values):
        path = os.path.join(os.path.dirname(__file__), 'templates', template_name)
        s = file(path,'rb').read()
        t = template.Template(s)
        c = template.Context(template_values)
        self.response.write(t.render(c))

class PageHandler(BaseHandler):
    def root(self):
        now = datetime.datetime.now()
        ten_min_ago = now - datetime.timedelta(minutes=10)
        context = {
            'now': now,
            'ten_min_ago': ten_min_ago
        }
        return self.render_template('django_pages_test_filters.html', context)


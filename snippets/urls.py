# -*- coding: utf-8 -*-
"""
Created on Fri May 06 13:48:42 2016

@author: UY57VX
"""

from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
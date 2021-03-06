#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from os import path

from flask import abort

from . import app
from . import config

# abort
app.add_template_global(abort)

# date
app.add_template_global(datetime.now().strftime, 'date')


@app.template_global()
def resource_join(rel_path):
    resource_dir = path.abspath(config['resources_folder'])
    return 'file://' + resource_dir + '/' + rel_path

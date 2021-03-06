#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import urljoin

from flask import render_template
from flask import render_template_string
from markupsafe import escape
from requests.exceptions import HTTPError

from . import config
from .filters import fetch_url


def _get_rule(rule):
    rule = escape(rule)
    return config['ruleset']['mapping'].get(rule, rule)


# serve local rule
def serve_local(rule):
    template_rule = f'ruleset/{_get_rule(rule)}'
    return render_template(template_rule)


# serve remote rule
def serve_remote(rule):
    for remote in config['ruleset']['remotes']:
        # add slash to remote url
        if not remote.endswith('/'):
            remote += '/'
        # join remote url
        rule_url = urljoin(remote, _get_rule(rule))
        try:
            text = fetch_url(rule_url)
            return render_template_string(text)
        except HTTPError:
            continue

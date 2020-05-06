#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Generali AG, Rene Fuehrer <rene.fuehrer@generali.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from sys import stderr, hexversion
import logging
from flask import Flask, request, abort


logging.basicConfig(stream=stderr, level=logging.INFO)

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def index():
    """
    Main WSGI application entry.
    """
    return "Hello World!"

if __name__ == '__main__':
    path = normpath(abspath(dirname(__file__)))
    app.run(debug=True, host='0.0.0.0', port=5000)

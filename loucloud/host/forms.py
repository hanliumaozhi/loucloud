#!/usr/bin/env python
# encoding: utf-8

from flask_wtf import Form
from wtforms import (TextField, SubmitField, IntegerField)


class AddHostForm(Form):
    name = TextField(u'名')
    username = TextField(u'用户名')
    password = TextField(u'密码')
    status_code = IntegerField(u'状态码')

    submit = SubmitField(u'创建')

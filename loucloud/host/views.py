#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template, request, redirect, url_for
from .forms import AddHostForm
from .models import Host
from ..dbs import db


host = Blueprint('host', __name__, url_prefix='/')


@host.route('', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = AddHostForm()
        host_list = Host.query.filter().all()
        return render_template("host/index.html", form=form, host_list=host_list)

    else:
        form = AddHostForm(request.form)
        if form.validate_on_submit():
            host_instance = Host()
            form.populate_obj(host_instance)
            db.session.add(host_instance)
            db.session.commit()
        return redirect(url_for('host.index'))


@host.route('host/<int:host_id>/delete', methods=['GET'])
def delete_host(host_id):
    host_instance = Host.query.filter(Host.id==host_id).first()
    if host_instance:
        db.session.delete(host_instance)
        db.session.commit()
    return redirect(url_for('host.index'))

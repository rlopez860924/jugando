# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Pets(models.Model):
    _name = 'pets'
    _description = _('Pets')

    name = fields.Char(string='name', required=True)
    age = fields.Integer(string='age')
    color = fields.Char(string='color')
    is_new = fields.Boolean(string='is_new')
    type = fields.Selection([('dog', 'Dog'),
                             ('cat', 'Cat'),
                             ('mouse', 'Mouse'),
                             ('rabbit','Rabbit'),
                             ('bird', 'Bird')], string='type', default="dog", required=True)

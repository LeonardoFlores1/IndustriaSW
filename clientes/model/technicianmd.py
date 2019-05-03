
# -*- coding: utf-8 -*-
from odoo import fields, models

class Usuarios(models.Model):
    _name = 'technician.usuarios'
    _description = 'tablad de usuarios'
    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email', required=True)
    password= fields.Char(string='Contraseña')
    phone= fields.Char(string='Telefono')
    rol_id= fields.one2Many(comodel_name='technician.rol', string='Userrol')
    dept_id=fields.one2Many(comodel_name='technician.dept', string='Department')
    
from odoo import models, fields

class VehicleMake(models.Model):
    _name = "vehicle.make"

    name = fields.Char(string="Brand", help='Vehicle make', required=True)
    
class VehicleModel(models.Model):
    _name = "vehicle.model"
    
    name = fields.Char(string="Model", help='Vehicle model', required=True)
    make_id = fields.Many2one('vehicle.make', string="Make", required=True)

from odoo import fields, models

class ParkingLot(models.Model):
    _name = 'parking.lot'
    _description = 'Parking Lot'

    name = fields.Char(string="Name", required=True, help='Parking lot name')
    address = fields.Char(string="Address", help='Parking lot address')
    capacity = fields.Integer(string="Capacity", default=0, required=True, help='Parking capacity')
    wash_service = fields.Boolean(string="Wash service", default=False, help='Washing service is available')
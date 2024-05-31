from odoo import fields, models

class ParkingVehicle(models.Model):
    _name = 'parking.vehicle'
    _description = 'Parking Vehicle'

    license_plate = fields.Char(string="Patente", required=True, help='Patente del Vehiculo')
    make = fields.Char(string="Marca", help='Marca')
    model = fields.Char(string="Modelo", help='Modelo')
    color = fields.Char(string="Color", help='Color')
    notes = fields.Text(string="Notas", help='Observaciones adicionales')
    entry_time = fields.Datetime(string="Hora de entrada", default=lambda self: fields.Datetime.now(), required=True, help='Hora de salida del vehiculo')
    exit_time = fields.Datetime(string="Hora de salida", help='Hora de salida del vehiculo')
    parking_lot_id = fields.Many2one('parking.lot', string="Parking Lot", required=True, help='Estacionamiento')
from odoo import fields, models

class ParkingLot(models.Model):
    _name = 'parking.lot'
    _description = 'Parking Lot'

    name = fields.Char(string="Nombre", required=True, help='Nombre del Estacionamiento')
    address = fields.Char(string="Dirección", help='Direccion del Estacionamiento')
    capacity = fields.Integer(string="Capacidad", default=0, required=True, help='Capantidad de lugares para estacionar')
    wash_service = fields.Boolean(string="Servicio de Lavado", help='Dispone de servicio de lavado')
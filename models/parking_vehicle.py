import re
from odoo import fields, models,api
import logging
_logger = logging.getLogger("BANANA")

class ParkingVehicle(models.Model):
    _name = 'parking.vehicle'
    _description = 'Parking Vehicle'

    name = fields.Char(string="Nombre", required=True)
    license_plate = fields.Char(string="License Plate", required=True, help='Vehicle license plate number')
    brand_id = fields.Many2one('vehicle.make', string='Make', help='Vehicle brand')
    model_id = fields.Many2one('vehicle.model', string='Model', help='Vehicle model')
    color = fields.Char(string="Color", help='Vehicle color')
    notes = fields.Text(string="Notes", help='Additional notes about the vehicle')
    entry_time = fields.Datetime(string="Entry Time", default=lambda self: fields.Datetime.now(), required=True, help='Time of vehicle entry')
    exit_time = fields.Datetime(string="Exit Time", help='Time of vehicle exit')
    parking_lot_id = fields.Many2one('parking.lot', string="Parking Lot", required=True, help='Parking lot')

    @api.onchange('license_plate')
    def _onchange_license_plate(self):

        if self.license_plate:
            license_plate = self.license_plate.strip()
            license_plate = license_plate.upper()
            self.license_plate = license_plate
            self.update({'name':license_plate})
            self['name'] = license_plate
            pattern = re.compile(r'^[A-Z0-9]+$')
            if not pattern.match(license_plate):
                return {
                    'warning': {
                        'title': "Invalid License Plate",
                        'message': "The license plate contains special characters. Please verify if it's correct.",
                        'type': 'notification'
                    }
                }
    
    @api.model_create_multi
    def create(self, vals_list):
        _logger.info("Se ha creado el registro")
        for val in vals_list:
            _logger.warning(val.get('license_plate'))
            _logger.warning(val['name'])
        return super().create(vals_list)
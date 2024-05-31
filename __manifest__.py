{
    'name': 'parking_fx',
    'version': '17.0.0.1.0',  # Versión WIP, módulo sin funcionalidades.
    'summary': 'Parking management module for Odoo',
    'description': """
        This module manages vehicle entry and exit in a parking lot.
        Features include:
        - Managing parking lots with their characteristics, and storing vehicles parked in each one
        - Collecting vehicle details such as license plate, make, model, color, and notes
        - Recording entry and exit times (TODO)
        - Handling payment details (TODO)
        - Vehicle banning functionality (TODO)
        - Reading external file for special conditions on license plates (TODO)
    """,
    'author': 'AgusCFx',
    'license': 'OPL-1',  # Odoo Proprietary License v1.0 (OPL-1)
    'category': 'Tools',
    'depends': [],
    'data':[
        'security/ir.model.access.csv',
        'views/parking_lot.xml',
        'views/parking_vehicle.xml',
        'views/menu.xml',
        ],
    'installable': True,
}
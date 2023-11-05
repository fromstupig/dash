from flask import current_app
from flask.cli import AppGroup, with_appcontext

from models.vehicle.vehicle import Vehicle
from models.vehicle.vehicle_model_style import VehicleModelStyle
from services import search

reindex_cli = AppGroup('reindex', help='Reindex elasticsearch data')


@reindex_cli.command('vehicle_model_styles', help='Reindex model_styles')
@with_appcontext
def reindex_vehicle_model_styles():
    if current_app.elastic_search.indices.exists(VehicleModelStyle.__tablename__):
        search.remove_index(VehicleModelStyle.__tablename__)
    search.reindex(VehicleModelStyle)


@reindex_cli.command('vehicles', help='Reindex vehicle')
@with_appcontext
def reindex_vehicle_model_styles():
    if current_app.elastic_search.indices.exists(Vehicle.__tablename__):
        search.remove_index(Vehicle.__tablename__)
    search.reindex(Vehicle)

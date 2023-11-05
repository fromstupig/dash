#!/usr/bin/env bash

flask core_provider countries -s ./seed/data/core_provider/countries.json
flask core_provider regions -s ./seed/data/core_provider/regions.json
flask core_provider states -s ./seed/data/core_provider/us_states.json
flask core_provider cities -s ./seed/data/core_provider/us_cities_zips.json
flask core_provider zip_codes -s ./seed/data/core_provider/us_cities_zips.json

flask seed vehicle_model_styles -s ./seed/data/vehicle/cars.json
flask reindex vehicle_model_styles
flask seed vehicle_gallery
flask seed vehicle_gallery_image
flask seed vehicle_color
flask seed vehicle
flask seed vehicle_model_galleries

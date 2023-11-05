import json
import random
from json import JSONDecodeError

import click
from flask import current_app
from flask.cli import AppGroup, with_appcontext

from models import db
from models.vehicle import VehicleBrand, VehicleModel, VehicleYearModel, VehicleModelStyle, VehicleBody, \
    VehicleCategory, VehicleDriveTrain, PriceVehicleModelStyleAssignment, PriceOptionAssignment, VehicleTransmission, \
    VehicleEngine, VehicleInfo, Vehicle, VehicleGalleryItem, VehicleOptionItem
import requests

from models.vehicle.vehicle_gallery_item import VehicleGalleryItemType
from models.vehicle.vehicle_option_item import VehicleOptionGroupType
from schemas.vehicle.vehicle_gallery_item import vehicle_gallery_item_schema, vehicle_gallery_items_schema
from schemas.vehicle.vehicle_model_style import vehicle_model_style_schema
from schemas.vehicle.vehicle_option_item import vehicle_option_item_schema, vehicle_option_items_schema

seed_cli = AppGroup('seed', help='Seed data')


@seed_cli.command('vehicle_brands', help='Seed vehicle brand data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_vehicle_brands(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        d_vehicle_brands = json.load(json_file)
        for d_vehicle_brand in d_vehicle_brands:
            is_exists = VehicleBrand.query.filter(VehicleBrand.name == d_vehicle_brand['make']).all()
            if is_exists:
                print(str(d_vehicle_brand['make']) + ' is exists.')
            else:
                vehicle_brand = VehicleBrand()
                # setattr(vehicle_brand, 'id', int(d_vehicle_brand['make_id']))
                setattr(vehicle_brand, 'name', d_vehicle_brand['make'])
                setattr(vehicle_brand, 'description', d_vehicle_brand['make'])
                db.session.add(vehicle_brand)
        db.session.commit()


@seed_cli.command('vehicle_models', help='Seed vehicle model data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_vehicle_models(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        d_vehicle_models = json.load(json_file)
        for d_vehicle_model in d_vehicle_models:
            is_exists = VehicleModel.query.filter(VehicleModel.description == int(d_vehicle_model['model_id']))
            if is_exists:
                print(str(d_vehicle_model['model_id']) + ' is exists.')
            else:
                vehicle_model = VehicleModel()
                setattr(vehicle_model, 'id', int(d_vehicle_model['model_id']))
                setattr(vehicle_model, 'name', d_vehicle_model['model'])
                setattr(vehicle_model, 'description', d_vehicle_model['make']
                        + ' ' + d_vehicle_model['model'])
                setattr(vehicle_model, 'vehicle_brand_id', int(d_vehicle_model['make_id']))
                db.session.add(vehicle_model)
        db.session.commit()


@seed_cli.command('vehicle_bodies', help='Seed vehicle body data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_bodies(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        d_bodies = json.load(json_file)
        for d_body in d_bodies:
            is_exists = VehicleBody.query.get(d_body['id'])
            if is_exists:
                print(str(d_body['id']) + ' is exists.')
            else:
                db.session.add(VehicleBody(**d_body))
        db.session.commit()


@seed_cli.command('vehicle_categories', help='Seed vehicle category data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_categories(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        d_categories = json.load(json_file)
        for d_category in d_categories:
            is_exists = VehicleCategory.query.get(d_category['id'])
            if is_exists:
                print(str(d_category['id']) + ' is exists.')
            else:
                db.session.add(VehicleCategory(**d_category))
        db.session.commit()


@seed_cli.command('vehicle_drive_trains', help='Seed vehicle category data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_drive_trains(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        d_drive_trains = json.load(json_file)
        for d_drive_train in d_drive_trains:
            is_exists = VehicleDriveTrain.query.get(d_drive_train['id'])
            if is_exists:
                print(str(d_drive_train['id']) + ' is exists.')
            else:
                db.session.add(VehicleDriveTrain(**d_drive_train))
        db.session.commit()


@seed_cli.command('vehicle_year_models', help='Seed vehicle year model data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_year_models(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        d_year_models = json.load(json_file)
        for d_year_model in d_year_models:
            is_exists = VehicleYearModel.query.filter(VehicleYearModel.vehicle_model_id == d_year_model['model_id']) \
                .filter(VehicleYearModel.year == d_year_model['year']).all()
            if is_exists:
                print(str(d_year_model['model_id']) + ' with year ' + d_year_model['year'] + ' is exists.')
            else:
                vehicle_year_model = VehicleYearModel()
                setattr(vehicle_year_model, 'name', d_year_model['make'] + ' ' + d_year_model['model'] \
                        + ' ' + d_year_model['year'])
                setattr(vehicle_year_model, 'description', d_year_model['make'] + ' ' + d_year_model['model'] \
                        + ' ' + d_year_model['year'])
                setattr(vehicle_year_model, 'year', d_year_model['year'])
                setattr(vehicle_year_model, 'vehicle_model_id', d_year_model['model_id'])
                db.session.add(vehicle_year_model)
        db.session.commit()


@seed_cli.command('vehicle_model_styles', help='Seed vehicle model style data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_model_styles(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        ds = json.load(json_file)
        for d in ds:
            brand = VehicleBrand.query.filter(VehicleBrand.name == d['make']).all()
            if brand:
                print(str(d['make']) + ' is exists.')
                vehicle_brand = brand[0]
            else:
                vehicle_brand = VehicleBrand()
                setattr(vehicle_brand, 'name', d['make'])
                setattr(vehicle_brand, 'description', d['make'])
                db.session.add(vehicle_brand)
                db.session.commit()

            model = VehicleModel.query.filter(VehicleModel.description == d['make'] + ' ' + d['model']).all()
            if model:
                print(str(d['model_id']) + ' is exists.')
                vehicle_model = model[0]
            else:
                vehicle_model = VehicleModel()
                setattr(vehicle_model, 'name', d['model'])
                setattr(vehicle_model, 'description', d['make'] + ' ' + d['model'])
                setattr(vehicle_model, 'vehicle_brand_id', vehicle_brand.id)
                db.session.add(vehicle_model)
                db.session.commit()

            year_model = VehicleYearModel.query.filter(VehicleYearModel.vehicle_model_id == vehicle_model.id) \
                .filter(VehicleYearModel.year == d['year']).all()
            if year_model:
                print(str(d['model_id']) + ' with year ' + d['year'] + ' is exists.')
                vehicle_year_model = year_model[0]
            else:
                vehicle_year_model = VehicleYearModel()
                setattr(vehicle_year_model, 'name', d['make'] + ' ' + d['model'] \
                        + ' ' + d['year'])
                setattr(vehicle_year_model, 'description', d['make'] + ' ' + d['model'] \
                        + ' ' + d['year'])
                setattr(vehicle_year_model, 'year', d['year'])
                setattr(vehicle_year_model, 'vehicle_model_id', vehicle_model.id)
                db.session.add(vehicle_year_model)
                db.session.commit()

            if 'model' in d['other_info']:
                d_model_styles = d['other_info']['model']['style']
                if not type(d_model_styles) in (tuple, list):
                    d_model_styles = [d_model_styles]

                for d_model_style in d_model_styles:
                    # seed body
                    body = VehicleBody.query.filter(VehicleBody.name == d_model_style['@bodyType']).all()
                    if body:
                        print(str(d_model_style['@bodyType']) + ' is exists.')
                        vehicle_body = body[0]
                    else:
                        vehicle_body = VehicleBody()
                        setattr(vehicle_body, 'name', d_model_style['@bodyType'])
                        setattr(vehicle_body, 'description', d_model_style['@bodyDescPrim'])
                        db.session.add(vehicle_body)
                        db.session.commit()

                    # seed drive train
                    drive_train = VehicleDriveTrain.query.filter(
                        VehicleDriveTrain.name == d_model_style['@drivetrain']).all()
                    if drive_train:
                        print(str(d_model_style['@drivetrain']) + ' is exists.')
                        vehicle_drive_train = drive_train[0]
                    else:
                        vehicle_drive_train = VehicleDriveTrain()
                        setattr(vehicle_drive_train, 'name', d_model_style['@drivetrain'])
                        setattr(vehicle_drive_train, 'description', d_model_style['@drivetrain'])
                        db.session.add(vehicle_drive_train)
                        db.session.commit()

                    # seed transmission
                    if d_model_style['@transType'] == "" or d_model_style['@transType'] == "N/A":
                        d_model_style['@transType'] = 0

                    transmission = VehicleTransmission.query.filter(
                        VehicleTransmission.label == d_model_style['@transDesc']) \
                        .filter(VehicleTransmission.speeds == int(d_model_style['@transType'])).all()
                    if transmission:
                        print(str(d_model_style['@transDesc']) + ' is exists.')
                        vehicle_transmission = transmission[0]
                    else:
                        vehicle_transmission = VehicleTransmission()
                        setattr(vehicle_transmission, 'label', d_model_style['@transDesc'])
                        setattr(vehicle_transmission, 'speeds', int(d_model_style['@transType']))
                        db.session.add(vehicle_transmission)
                        db.session.commit()

                    # seed engine
                    engine = VehicleEngine.query.filter(VehicleEngine.label == (d_model_style['@engineType']
                                                                                + ' ' + d_model_style[
                                                                                    '@engineDisplacement'])).all()
                    if engine:
                        print(str(d_model_style['@engineType']) + ' is exists.')
                        vehicle_engine = engine[0]
                    else:
                        vehicle_engine = VehicleEngine()
                        setattr(vehicle_engine, 'label', d_model_style['@engineType']
                                + ' ' + d_model_style['@engineDisplacement'])
                        db.session.add(vehicle_engine)
                        db.session.commit()

                    is_exists = VehicleModelStyle.query.filter(
                        VehicleModelStyle.name == d_model_style['@fullDisplayName']).all()
                    if is_exists:
                        print(str(d_model_style['@fullDisplayName']) + ' is exists.')
                    else:
                        vehicle_model_style = VehicleModelStyle()
                        setattr(vehicle_model_style, 'name', d_model_style['@fullDisplayName'])
                        setattr(vehicle_model_style, 'description', d_model_style['@name'])
                        setattr(vehicle_model_style, 'vehicle_year_model_id', vehicle_year_model.id)
                        if 'details' in d_model_style:
                            setattr(vehicle_model_style, 'standard_feature', d_model_style["details"])
                        if 'new_pricing_options' in d_model_style:
                            setattr(vehicle_model_style, 'pricing_options', d_model_style['new_pricing_options'])
                        if 'technical_info' in d_model_style:
                            setattr(vehicle_model_style, 'technical_feature', d_model_style['technical_info'])
                        if 'consumer_info' in d_model_style:
                            setattr(vehicle_model_style, 'consumer_info', d_model_style['consumer_info'])

                        setattr(vehicle_model_style, 'drive_trains', [{'id': vehicle_drive_train.id}])
                        setattr(vehicle_model_style, 'transmissions', [{'id': vehicle_transmission.id}])
                        setattr(vehicle_model_style, 'engines', [{'id': vehicle_engine.id}])
                        setattr(vehicle_model_style, 'body_id', vehicle_body.id)
                        if d_model_style["@baseMSRP"] == 'N/A':
                            d_model_style["@baseMSRP"] = "0"
                        setattr(vehicle_model_style, 'base_MSRP',
                                str.replace(d_model_style["@baseMSRP"], '$', '').replace(',', ''))
                        setattr(vehicle_model_style, 'manufacture_code', d_model_style["@manufactureCode"])
                        setattr(vehicle_model_style, 'image_url', d_model_style["@imageUrl"])
                        db.session.add(vehicle_model_style)
                        db.session.commit()


@seed_cli.command('vehicle_model_style_options', help='Seed vehicle_model_style_options data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_vehicle_model_style_options(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        options = json.load(json_file)
        d_vehicle_model_styles = VehicleModelStyle.query.all()
        for d_vehicle_model_style in d_vehicle_model_styles:
            setattr(d_vehicle_model_style, 'options', options)
            db.session.commit()


@seed_cli.command('vehicle_gallery', help='Seed vehicle gallery vif num data.')
@with_appcontext
def seed_vehicle_gallery():
    print("Start seed vehicle gallery ")
    headers = {'x-api-key': current_app.config["EVOX_API_KEY"]}
    d_vehicle_model_styles = VehicleModelStyle.query.all()
    for d_vehicle_model_style in d_vehicle_model_styles:
        if d_vehicle_model_style.vif_num is None:
            params = {
                'model': d_vehicle_model_style.vehicle_year_model.vehicle_model.name,
                'year': d_vehicle_model_style.vehicle_year_model.year,
                'make': d_vehicle_model_style.vehicle_year_model.vehicle_model.vehicle_brand.name
            }
            print(params)
            r_vehicle = requests.get(current_app.config["EVOX_API_URL"] + '/vehicles', headers=headers, params=params)
            result = r_vehicle.json()
            print(result)
            if 'data' in result:
                trims = result['data']
                vif_num = 0
                print('----------')
                print('search in ' + str(len(trims)) + ' for ' + d_vehicle_model_style.name)
                for trim in trims:
                    # print(trim['trim'])
                    if trim['trim'] is not None:
                        if all(word in d_vehicle_model_style.name for word in trim['trim']):
                            vif_num = trim['vifnum']
                            break
                print('vifnum for ' + d_vehicle_model_style.name + ': ' + str(vif_num))
                print('----------')
                setattr(d_vehicle_model_style, 'vif_num', vif_num)
                db.session.commit()


@seed_cli.command('vehicle_gallery_image', help='Seed vehicle gallery data.')
@with_appcontext
def seed_vehicle_gallery_image():
    headers = {'x-api-key': current_app.config["EVOX_API_KEY"]}
    d_vehicle_model_styles = VehicleModelStyle.query.all()
    # print(vehicle_model_style_schema.dumps(d_vehicle_model_styles[0]))
    last_vif_num = -1
    for d_vehicle_model_style in d_vehicle_model_styles:
        if d_vehicle_model_style.vif_num is not None and d_vehicle_model_style.vif_num > 0:
            current_galleries = getattr(d_vehicle_model_style, 'galleries')
            if len(current_galleries) == 0:
                print(str(d_vehicle_model_style.vif_num))
                print(str(d_vehicle_model_style.id))
                if d_vehicle_model_style.vif_num == last_vif_num:
                    print(len(vgis))
                    setattr(d_vehicle_model_style, 'galleries', vehicle_gallery_items_schema.dump(vgis))
                    db.session.commit()
                else:
                    # vgis = getattr(d_vehicle_model_style, 'galleries')
                    vgis = []
                    r_vehicle_color = requests.get(
                        current_app.config["EVOX_API_URL"] + '/vehicles/' + str(d_vehicle_model_style.vif_num)
                        + '/products/2/44', headers=headers)

                    try:
                        result = r_vehicle_color.json()
                        if 'urls' in result:
                            urls = result['urls']
                            index = 0
                            for url in urls:
                                vgi = VehicleGalleryItem()
                                vgi.asset_path = url
                                vgi.type = VehicleGalleryItemType.EXTERIOR_COLOR
                                vgi.order = index
                                vgis.append(vgi)
                                index += 1
                        else:
                            print('VehicleGalleryItemType.EXTERIOR_COLOR NOT FOUND')
                    except JSONDecodeError:
                        print(r_vehicle_color)
                        print('JSONDecodeError')

                    r_vehicle_interior_spin = requests.get(
                        current_app.config["EVOX_API_URL"] + '/vehicles/' + str(d_vehicle_model_style.vif_num)
                        + '/products/12/122', headers=headers)
                    try:
                        result = r_vehicle_interior_spin.json()
                        if 'urls' in result:
                            urls = result['urls']
                            index = 0
                            for url in urls:
                                vgi = VehicleGalleryItem()
                                vgi.asset_path = url
                                vgi.type = VehicleGalleryItemType.INTERIOR
                                vgi.order = index
                                vgis.append(vgi)
                                index += 1
                        else:
                            print('VehicleGalleryItemType.INTERIOR NOT FOUND')
                    except JSONDecodeError:
                        print(r_vehicle_interior_spin)
                        print('JSONDecodeError')

                    r_vehicle_exterior_spin = requests.get(
                        current_app.config["EVOX_API_URL"] + '/vehicles/' + str(d_vehicle_model_style.vif_num)
                        + '/products/3/69', headers=headers)
                    try:
                        result = r_vehicle_exterior_spin.json()
                        if 'urls' in result:
                            urls = result['urls']
                            index = 0
                            for url in urls:
                                vgi = VehicleGalleryItem()
                                vgi.asset_path = url
                                vgi.type = VehicleGalleryItemType.EXTERIOR
                                vgi.order = index
                                vgis.append(vgi)
                                index += 1
                        else:
                            print('VehicleGalleryItemType.EXTERIOR NOT FOUND')
                    except JSONDecodeError:
                        print(r_vehicle_exterior_spin)
                        print('JSONDecodeError')

                    # print(vehicle_gallery_items_schema.dump(vgis))
                    setattr(d_vehicle_model_style, 'galleries', vehicle_gallery_items_schema.dump(vgis))
                    db.session.commit()
                last_vif_num = d_vehicle_model_style.vif_num


# 3-Angle Colorized Set (Product ID 2 - 50 - 1280)
# Interior Panos (Product ID 12 - 122 - 1280)
# Exterior Spins (Product ID 3 - 69 - 1280)
# Mapping (Product ID 25)
# Viflist (Product ID 26)

@seed_cli.command('vehicle_color', help='Seed vehicle gallery color.')
@with_appcontext
def seed_vehicle_gallery_color():
    headers = {'x-api-key': current_app.config["EVOX_API_KEY"]}
    d_vehicle_model_styles = VehicleModelStyle.query.all()
    # print(vehicle_model_style_schema.dumps(d_vehicle_model_styles[0]))
    for d_vehicle_model_style in d_vehicle_model_styles:
        if d_vehicle_model_style.vif_num is not None and d_vehicle_model_style.vif_num > 0:
            print(str(d_vehicle_model_style.vif_num))
            options = []
            r_vehicle_color = requests.get(
                current_app.config["EVOX_API_URL"] + '/vehicles/' + str(d_vehicle_model_style.vif_num)
                + '/colors', headers=headers)
            result = r_vehicle_color.json()
            if 'data' in result:
                if 'colors' in result['data']:
                    colors = result['data']['colors']
                    for color in colors:
                        print(color)
                        voi = VehicleOptionItem()
                        voi.description = color['title'] if color['title'] is not None else color['simpletitle']
                        voi.detail = color
                        voi.type = VehicleOptionGroupType.EXTERIOR_COLOR
                        voi.is_popular = False
                        options.append(voi)
                else:
                    print('EXTERIOR_COLOR NOT FOUND')
                setattr(d_vehicle_model_style, 'options', vehicle_option_items_schema.dump(options))
                db.session.commit()


@seed_cli.command('vehicle', help='Seed vehicle data.')
@with_appcontext
def seed_vehicle():
    d_vehicle_model_styles = VehicleModelStyle.query.all()
    index = 0
    for d_vehicle_model_style in d_vehicle_model_styles:
        if d_vehicle_model_style.vif_num is not None and d_vehicle_model_style.vif_num > 0:
            if len(d_vehicle_model_style.options) > 0:
                print(d_vehicle_model_style.vif_num)
                r_color = random.randint(0, len(d_vehicle_model_style.options) - 1)
                json_voi = vehicle_option_item_schema.dump(d_vehicle_model_style.options[r_color])
                del json_voi['id']
                del json_voi['current_price_assigment']
                print(json_voi)
                r_num_vehicle = random.randint(1, 10)
                for x in range(1, r_num_vehicle):
                    options = [json_voi]
                    vehicle = Vehicle()
                    vehicle.vehicle_model_style_id = d_vehicle_model_style.id
                    setattr(vehicle, 'id', index)
                    setattr(vehicle, 'vehicle_brand_id',
                            d_vehicle_model_style.vehicle_year_model.vehicle_model.vehicle_brand.id)
                    setattr(vehicle, 'vehicle_model_id', d_vehicle_model_style.vehicle_year_model.vehicle_model.id)
                    setattr(vehicle, 'vehicle_model_style_id', d_vehicle_model_style.id)
                    setattr(vehicle, 'custom_options', options)
                    db.session.add(vehicle)
                    db.session.commit()
                    index += 1


@seed_cli.command('vehicle_model_style_prices', help='Seed vehicle model style prices data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_model_style_prices(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        d_model_style_prices = json.load(json_file)
        for d_model_style_price in d_model_style_prices:
            is_exists = PriceVehicleModelStyleAssignment.query.get(d_model_style_price['id'])
            if is_exists:
                print(str(d_model_style_price['id']) + ' is exists.')
            else:
                db.session.add(PriceVehicleModelStyleAssignment(**d_model_style_price))
        db.session.commit()


@seed_cli.command('vehicle_option_prices', help='Seed vehicle option prices data.')
@click.option('-s', '--source', nargs=1, type=click.STRING, help='Json Data Source', required=True)
@with_appcontext
def seed_option_prices(source):
    with open(source, encoding='utf-8-sig', errors='ignore') as json_file:
        d_option_prices = json.load(json_file)
        for d_option_price in d_option_prices:
            is_exists = PriceOptionAssignment.query.get(d_option_price['id'])
            if is_exists:
                print(str(d_option_price['id']) + ' is exists.')
            else:
                db.session.add(PriceOptionAssignment(**d_option_price))
        db.session.commit()


@seed_cli.command('vehicle_model_galleries', help='Seed vehicle model gallery.')
@with_appcontext
def seed_vehicle_model_galleries():
    d_vehicle_models = VehicleModel.query.all()
    for d_vehicle_model in d_vehicle_models:
        vgis = getattr(d_vehicle_model, 'galleries')
        d_year_model = VehicleYearModel.query.filter(VehicleYearModel.vehicle_model_id == d_vehicle_model.id).first()
        if d_year_model:
            d_model_style = VehicleModelStyle.query.filter(
                VehicleModelStyle.vehicle_year_model_id == d_year_model.id).first()
            if d_model_style:
                model_style_gallery = \
                    list(filter(lambda x: x.type == VehicleGalleryItemType.EXTERIOR_COLOR, d_model_style.galleries))
                if len(model_style_gallery) > 0:
                    print(model_style_gallery[0].asset_path)
                    vgi = VehicleGalleryItem()
                    vgi.asset_path = model_style_gallery[0].asset_path
                    vgi.type = VehicleGalleryItemType.MODEL_AVATAR
                    vgi.order = 0
                    vgis.append(vgi)
                    setattr(d_vehicle_model, 'galleries', vehicle_gallery_items_schema.dump(vgis))
                    db.session.commit()

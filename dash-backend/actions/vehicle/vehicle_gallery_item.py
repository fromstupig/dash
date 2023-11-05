from models import db
from models.vehicle.vehicle_gallery_item import VehicleGalleryItem
from schemas.vehicle.vehicle_gallery_item import vehicle_gallery_item_schema, vehicle_gallery_items_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException, BadRequestException


class VehicleGalleryItemAction:
    def create(self, data):
        validated_data = vehicle_gallery_item_schema.load(data)
        entity = VehicleGalleryItem(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return vehicle_gallery_item_schema.dump(entity)

    def create_gallery_items(self, gallery_item_type, files):
        if files is None:
            raise BadRequestException(detail='There is no files to process')
        media = media_action.upload_file_to_s3(files)
        a_galleries = []
        for index, media_item in enumerate(media):
            gallery_item_data = dict(
                type=gallery_item_type,
                asset_path=media_item['public_id'],
                order=index
            )
            a_galleries.append(VehicleGalleryItem(**gallery_item_data))

        return a_galleries

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = VehicleGalleryItem.query
        query = query.filter(VehicleGalleryItem.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                VehicleGalleryItem.id.asc()) if direction == SortDirection.ASC else query.order_by(
                VehicleGalleryItem.id.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = vehicle_gallery_items_schema.dump(items)

        return rv, total

    def update(self, id_, data):
        current_vehicle_gallery_item = VehicleGalleryItem.query.get(id_)
        if not current_vehicle_gallery_item:
            raise EntityNotFoundException(id_, 'VehicleGalleryItem')

        validated_data = vehicle_gallery_item_schema.load(data)
        validated_data['id'] = None
        entity = VehicleGalleryItem(**validated_data)
        db.session.add(entity)

        db.session.commit()
        return vehicle_gallery_item_schema.dump(entity)

    def delete(self, id_):
        vehicle_gallery_item = VehicleGalleryItem.query.get(id_)
        if not vehicle_gallery_item:
            raise EntityNotFoundException(id_, 'VehicleGalleryItem')

        db.session.delete(vehicle_gallery_item)
        db.session.commit()

    def delete_by_gallery_id(self, gallery_id):
        vehicle_gallery_items = VehicleGalleryItem.query.filter(VehicleGalleryItem.gallery_id == gallery_id).all()
        for vehicle_gallery_item in vehicle_gallery_items:
            db.session.delete(vehicle_gallery_item)
        db.session.commit()


vehicle_gallery_item_action = VehicleGalleryItemAction()

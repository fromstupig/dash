from models import db
from models.vehicle.price_option_assignment import PriceOptionAssignment
from schemas.vehicle.price_option_assignment import price_option_assignment_schema, price_option_assignments_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class PriceOptionAssignmentAction:
    def create(self, data):
        validated_data = price_option_assignment_schema.load(data)
        entity = PriceOptionAssignment(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return price_option_assignment_schema.dump(entity)

    def get(self, id_):
        current_price_option_assignment = PriceOptionAssignment.query.get(id_)
        if not current_price_option_assignment:
            raise EntityNotFoundException(id_, 'PriceOptionAssignment')
        else:
            return price_option_assignment_schema.dump(current_price_option_assignment)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = PriceOptionAssignment.query
        query = query.filter(PriceOptionAssignment.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                PriceOptionAssignment.start_date.asc()) if direction == SortDirection.ASC else query.order_by(
                PriceOptionAssignment.start_date.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = price_option_assignments_schema.dump(items)

        return rv, total

    def update(self, id_, data):
        current_price_option_assignment = PriceOptionAssignment.query.get(id_)
        if not current_price_option_assignment:
            raise EntityNotFoundException(id_, 'PriceOptionAssignment')

        validated_data = price_option_assignment_schema.load(data)
        validated_data['id'] = None
        entity = PriceOptionAssignment(**validated_data)
        db.session.add(entity)

        db.session.commit()
        return price_option_assignment_schema.dump(entity)

    def delete(self, id_):
        price_option_assignment = PriceOptionAssignment.query.get(id_)
        if not price_option_assignment:
            raise EntityNotFoundException(id_, 'PriceOptionAssignment')

        db.session.delete(price_option_assignment)
        db.session.commit()


price_option_assignment_action = PriceOptionAssignmentAction()

from models import db
from models.dealer.dealer import Dealer
from schemas.dealer.dealer import dealer_schema, dealers_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class DealerAction:
    def create(self, data):
        validated_data = dealer_schema.load(data)
        entity = Dealer(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return dealer_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = Dealer.query if q == '' else Dealer.query.filter(Dealer.name.like('%{}%'.format(q)))
        query = query.filter(Dealer.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                Dealer.name.asc()) if direction == SortDirection.ASC else query.order_by(
                Dealer.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = dealers_schema.dump(items)

        return rv, total

    def get(self, id_):
        current_dealer = Dealer.query.get(id_)
        if not current_dealer:
            raise EntityNotFoundException(id_, 'Dealer')

        return dealer_schema.dump(current_dealer)

    def update(self, id_, data):
        current_dealer = Dealer.query.get(id_)
        if not current_dealer:
            raise EntityNotFoundException(id_, 'Dealer')

        validated_data = dealer_schema.load(data)
        validated_data['id'] = None
        current_dealer.update(validated_data)
        db.session.commit()

        return dealer_schema.dump(current_dealer)

    def delete(self, id_):
        dealer = Dealer.query.get(id_)
        if not dealer:
            raise EntityNotFoundException(id_, 'Dealer')

        db.session.delete(dealer)
        db.session.commit()


dealer_action = DealerAction()

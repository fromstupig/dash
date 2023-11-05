from models import db
from models.dealer.dealer_request import DealerRequest
from schemas.dealer.dealer_request import dealer_request_schema, dealer_requests_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class DealerRequestAction:
    def create(self, data):
        validated_data = dealer_request_schema.load(data)
        entity = DealerRequest(**validated_data)
        db.session.add(entity)
        db.session.commit()
        return dealer_request_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = DealerRequest.query if q == '' else DealerRequest.query.filter(
            DealerRequest.requester_email.like('%{}%'.format(q)))
        query = query.filter(DealerRequest.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                DealerRequest.modification_date.asc()) if direction == SortDirection.ASC else query.order_by(
                DealerRequest.modification_date.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = dealer_requests_schema.dump(items)

        return rv, total

    def get_all_by_current_user(self, user_id, sort, direction, limit, offset, is_active, q=''):
        query = DealerRequest.query if q == '' else DealerRequest.query.filter(
            DealerRequest.requester_email.like('%{}%'.format(q)))
        query = query.filter(DealerRequest.is_active == is_active) if is_active is not None else query
        query = query.filter(DealerRequest.user_id == user_id)
        if sort:
            query = query.order_by(
                DealerRequest.modification_date.asc()) if direction == SortDirection.ASC else query.order_by(
                DealerRequest.modification_date.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = dealer_requests_schema.dump(items)

        return rv, total

    def get(self, id_):
        current_dealer_request = DealerRequest.query.get(id_)
        if not current_dealer_request:
            raise EntityNotFoundException(id_, 'DealerRequest')

        return dealer_request_schema.dump(current_dealer_request)

    def update(self, id_, data):
        current_dealer_request = DealerRequest.query.get(id_)
        if not current_dealer_request:
            raise EntityNotFoundException(id_, 'DealerRequest')

        validated_data = dealer_request_schema.load(data)
        validated_data['id'] = None
        current_dealer_request.update(validated_data)
        db.session.commit()

        return dealer_request_schema.dump(current_dealer_request)

    def delete(self, id_):
        dealer = DealerRequest.query.get(id_)
        if not dealer:
            raise EntityNotFoundException(id_, 'DealerRequest')

        db.session.delete(dealer)
        db.session.commit()


dealer_request_action = DealerRequestAction()

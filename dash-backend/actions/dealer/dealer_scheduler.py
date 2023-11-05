import calendar
import datetime

from flask import current_app
from sqlalchemy import and_

from config import config
from models import db
from models.dealer.dealer_scheduler import DealerScheduler
from schemas.dealer.dealer_scheduler import dealer_scheduler_schema, dealer_schedulers_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException, InvalidRequestException, BadRequestException


class DealerSchedulerAction:
    def create(self, data):
        validated_data = dealer_scheduler_schema.load(data)
        if 'schedule_time' in validated_data and 'dealer_id' in validated_data:
            minutes_to_add = current_app.config['SCHEDULER_DEFAULT_TIMESPAN']
            schedule_time_end = validated_data['schedule_time'] + datetime.timedelta(minutes=minutes_to_add)
            query = DealerScheduler.query.filter(DealerScheduler.dealer_id == validated_data['dealer_id'])
            total = query.filter(and_(DealerScheduler.schedule_time >= validated_data['schedule_time'],
                                      DealerScheduler.schedule_time <= schedule_time_end)).count()
            if total >= current_app.config['SCHEDULER_DEFAULT_MAX_SESSION']:
                raise BadRequestException(detail="Maximum slot exceed")
            else:
                entity = DealerScheduler(**validated_data)
                db.session.add(entity)
                db.session.commit()
                return dealer_scheduler_schema.dump(entity)
        else:
            raise BadRequestException()

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = DealerScheduler.query if q == '' else DealerScheduler.query.filter(
            DealerScheduler.schedule_title.like('%{}%'.format(q)))
        query = query.filter(DealerScheduler.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                DealerScheduler.schedule_time.asc()) if direction == SortDirection.ASC else query.order_by(
                DealerScheduler.schedule_time.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = dealer_schedulers_schema.dump(items)

        return rv, total

    def get_monthly_scheduler_by_dealer(self, dealer_id, month_num):
        if dealer_id is not None and month_num is not None:

            current_year = datetime.datetime.now().year
            num_days = calendar.monthrange(current_year, month_num)[1]
            start_date = datetime.date(current_year, month_num, 1)
            end_date = datetime.date(current_year, month_num, num_days)

            query = DealerScheduler.query.filter(DealerScheduler.dealer_id == dealer_id)
            query = query.filter(and_(DealerScheduler.schedule_time >= start_date,
                                      DealerScheduler.schedule_time <= end_date))
            query = query.order_by(DealerScheduler.schedule_time.asc())

            total = query.count()
            items = query.all()

            rv = dealer_schedulers_schema.dump(items)

            return rv, total
        else:
            raise InvalidRequestException(code='Invalid Dealer or Month')

    def get(self, id_):
        current_dealer_scheduler = DealerScheduler.query.get(id_)
        if not current_dealer_scheduler:
            raise EntityNotFoundException(id_, 'DealerScheduler')

        return dealer_scheduler_schema.dump(current_dealer_scheduler)

    def update(self, id_, data):
        current_dealer_scheduler = DealerScheduler.query.get(id_)
        if not current_dealer_scheduler:
            raise EntityNotFoundException(id_, 'DealerScheduler')

        validated_data = dealer_scheduler_schema.load(data)
        validated_data['id'] = None
        current_dealer_scheduler.update(validated_data)
        db.session.commit()

        return dealer_scheduler_schema.dump(current_dealer_scheduler)

    def delete(self, id_):
        dealer = DealerScheduler.query.get(id_)
        if not dealer:
            raise EntityNotFoundException(id_, 'DealerScheduler')

        db.session.delete(dealer)
        db.session.commit()


dealer_scheduler_action = DealerSchedulerAction()

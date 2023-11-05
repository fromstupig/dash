from models import db
from models.authorization.tenant import Tenant
from schemas.authorization.tenant import tenant_schema, tenant_schemas, tenant_update_schema
from utilities.enum import SortDirection
from utilities.exception import EntityNotFoundException


class TenantAction:
    def create(self, data):
        validated_data = tenant_schema.load(data)
        entity = Tenant(**validated_data)

        db.session.add(entity)
        db.session.commit()

        return tenant_schema.dump(entity)

    def get_all(self, sort, direction, limit, offset, is_active, q=''):
        query = Tenant.query.filter(Tenant.name.like('%{}%'.format(q)))
        query = query.filter(Tenant.is_active == is_active) if is_active is not None else query

        if sort:
            query = query.order_by(
                Tenant.name.asc()) if direction == SortDirection.ASC else query.order_by(
                Tenant.name.desc())

        total = query.count()
        items = query.limit(limit).offset(offset).all()

        rv = tenant_schemas.dump(items)

        return rv, total

    def update(self, id_, data):
        model = Tenant.query.get(id_)
        if not model:
            raise EntityNotFoundException(id_, 'Tenant')

        update_model = tenant_update_schema.load(data)
        model.update(update_model)

        db.session.commit()
        return tenant_schema.dump(model)

    def delete(self, id_):
        tenant = Tenant.query.get(id_)
        if not tenant:
            raise EntityNotFoundException(id_, 'Tenant')

        db.session.delete(tenant)
        db.session.commit()


tenant_action = TenantAction()

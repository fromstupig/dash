"""add pricing options for model style

Revision ID: 3a2322ff2503
Revises: 018f7ac7fd8c
Create Date: 2020-10-21 23:04:47.838409

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3a2322ff2503'
down_revision = '018f7ac7fd8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vehicle_model_styles',
                  sa.Column('pricing_options', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vehicle_model_styles', 'pricing_options')
    # ### end Alembic commands ###

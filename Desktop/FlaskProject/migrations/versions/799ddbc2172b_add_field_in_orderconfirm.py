"""add field in OrderConfirm

Revision ID: 799ddbc2172b
Revises: dd9dfa3994e5
Create Date: 2022-06-06 13:55:41.687987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '799ddbc2172b'
down_revision = 'dd9dfa3994e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_confirm', sa.Column('address', sa.String(length=300), nullable=True))
    op.add_column('order_confirm', sa.Column('subDistrict', sa.String(length=40), nullable=True))
    op.add_column('order_confirm', sa.Column('district', sa.String(length=40), nullable=True))
    op.add_column('order_confirm', sa.Column('province', sa.String(length=40), nullable=True))
    op.add_column('order_confirm', sa.Column('postCode', sa.String(length=10), nullable=True))
    op.add_column('order_confirm', sa.Column('telephone', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order_confirm', 'telephone')
    op.drop_column('order_confirm', 'postCode')
    op.drop_column('order_confirm', 'province')
    op.drop_column('order_confirm', 'district')
    op.drop_column('order_confirm', 'subDistrict')
    op.drop_column('order_confirm', 'address')
    # ### end Alembic commands ###

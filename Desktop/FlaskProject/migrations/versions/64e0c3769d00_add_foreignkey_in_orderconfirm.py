"""add foreignkey in OrderConfirm

Revision ID: 64e0c3769d00
Revises: e3cba61ed4c9
Create Date: 2022-06-06 15:02:05.629995

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '64e0c3769d00'
down_revision = 'e3cba61ed4c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_confirm', sa.Column('item', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'order_confirm', 'product_data', ['item'], ['id'])
    op.drop_column('order_confirm', 'code')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_confirm', sa.Column('code', mysql.VARCHAR(length=20), nullable=True))
    op.drop_constraint(None, 'order_confirm', type_='foreignkey')
    op.drop_column('order_confirm', 'item')
    # ### end Alembic commands ###
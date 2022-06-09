"""reset

Revision ID: f47b1b4f36cf
Revises: 64e0c3769d00
Create Date: 2022-06-06 15:51:57.361834

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f47b1b4f36cf'
down_revision = '64e0c3769d00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_confirm', sa.Column('code', sa.String(length=40), nullable=True))
    op.add_column('order_confirm', sa.Column('client', sa.String(length=40), nullable=True))
    op.drop_constraint('order_confirm_ibfk_2', 'order_confirm', type_='foreignkey')
    op.drop_constraint('order_confirm_ibfk_1', 'order_confirm', type_='foreignkey')
    op.drop_column('order_confirm', 'item')
    op.drop_column('order_confirm', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_confirm', sa.Column('address', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('order_confirm', sa.Column('item', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('order_confirm_ibfk_1', 'order_confirm', 'address', ['address'], ['id'])
    op.create_foreign_key('order_confirm_ibfk_2', 'order_confirm', 'product_data', ['item'], ['id'])
    op.drop_column('order_confirm', 'client')
    op.drop_column('order_confirm', 'code')
    # ### end Alembic commands ###
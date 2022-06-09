"""OrderConfirm add ForeignKey

Revision ID: b7a9171a0091
Revises: f5eca53a4fa9
Create Date: 2022-06-06 16:21:13.301893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7a9171a0091'
down_revision = 'f5eca53a4fa9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'order_confirm', 'product_data', ['item'], ['id'])
    op.create_foreign_key(None, 'order_confirm', 'address', ['client'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order_confirm', type_='foreignkey')
    op.drop_constraint(None, 'order_confirm', type_='foreignkey')
    # ### end Alembic commands ###
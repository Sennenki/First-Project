"""add ProductData table

Revision ID: 7c74d3108a5e
Revises: 413ac725ffb0
Create Date: 2022-05-27 17:22:05.683473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c74d3108a5e'
down_revision = '413ac725ffb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=2), nullable=True),
    sa.Column('group', sa.String(length=2), nullable=True),
    sa.Column('code', sa.String(length=20), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('price', sa.String(length=10), nullable=True),
    sa.Column('deal', sa.String(length=50), nullable=True),
    sa.Column('file', sa.String(length=50), nullable=True),
    sa.Column('date_log', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_data')
    # ### end Alembic commands ###
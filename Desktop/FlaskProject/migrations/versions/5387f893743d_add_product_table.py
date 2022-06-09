"""add Product table

Revision ID: 5387f893743d
Revises: 358d738bdb5c
Create Date: 2022-05-27 17:02:36.694448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5387f893743d'
down_revision = '358d738bdb5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
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
    op.drop_table('product')
    # ### end Alembic commands ###
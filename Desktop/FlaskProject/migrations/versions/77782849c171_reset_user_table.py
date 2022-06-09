"""reset user table

Revision ID: 77782849c171
Revises: a0d288bdacf7
Create Date: 2022-05-26 20:02:59.416510

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '77782849c171'
down_revision = 'a0d288bdacf7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'activity')
    op.drop_column('user', 'color')
    op.drop_column('user', 'name')
    op.drop_column('user', 'gender')
    op.drop_column('user', 'age')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('age', mysql.VARCHAR(length=3), nullable=True))
    op.add_column('user', sa.Column('gender', mysql.VARCHAR(length=1), nullable=True))
    op.add_column('user', sa.Column('name', mysql.VARCHAR(length=100), nullable=True))
    op.add_column('user', sa.Column('color', mysql.VARCHAR(length=30), nullable=True))
    op.add_column('user', sa.Column('activity', mysql.VARCHAR(length=1), nullable=True))
    # ### end Alembic commands ###
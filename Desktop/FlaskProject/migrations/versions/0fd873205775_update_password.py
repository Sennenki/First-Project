"""update password

Revision ID: 0fd873205775
Revises: 681d43caed1e
Create Date: 2022-06-09 15:04:19.145265

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0fd873205775'
down_revision = '681d43caed1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('encrypt_password', sa.String(length=128), nullable=True))
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=128), nullable=True))
    op.drop_column('user', 'encrypt_password')
    # ### end Alembic commands ###

"""add image column

Revision ID: 27610b9f313e
Revises: f39bd78c1131
Create Date: 2022-05-29 21:03:28.832730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27610b9f313e'
down_revision = 'f39bd78c1131'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('file', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'file')
    # ### end Alembic commands ###

"""rename address

Revision ID: 1900424ac29e
Revises: 72c488713707
Create Date: 2024-09-03 21:19:51.086890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1900424ac29e'
down_revision = '72c488713707'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###

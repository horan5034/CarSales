"""Add Mileage To UsedStock

Revision ID: f42702ba3f18
Revises: bc801384938f
Create Date: 2017-08-29 20:23:05.042000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f42702ba3f18'
down_revision = 'bc801384938f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('used_stock', sa.Column('mileage', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('used_stock', 'mileage')
    # ### end Alembic commands ###

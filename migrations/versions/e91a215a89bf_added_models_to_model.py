"""Added Models to Model

Revision ID: e91a215a89bf
Revises: f2c054d04cc9
Create Date: 2017-09-01 19:15:00.101000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e91a215a89bf'
down_revision = 'f2c054d04cc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('make_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['make_id'], ['makes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'used_stock', sa.Column('model_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'used_stock', 'models', ['model_id'], ['id'])
    op.drop_column(u'used_stock', 'model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'used_stock', sa.Column('model', mysql.VARCHAR(length=100), nullable=False))
    op.drop_constraint(None, 'used_stock', type_='foreignkey')
    op.drop_column(u'used_stock', 'model_id')
    op.drop_table('models')
    # ### end Alembic commands ###

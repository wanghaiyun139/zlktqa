"""empty message

Revision ID: 665b177a72a0
Revises: 1a1e0c395ff3
Create Date: 2017-06-18 15:37:32.313000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '665b177a72a0'
down_revision = '1a1e0c395ff3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answers', 'create_time')
    # ### end Alembic commands ###

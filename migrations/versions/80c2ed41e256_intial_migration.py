"""Intial migration

Revision ID: 80c2ed41e256
Revises: 
Create Date: 2024-09-09 16:28:54.759776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80c2ed41e256'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bio', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('bio')

    # ### end Alembic commands ###

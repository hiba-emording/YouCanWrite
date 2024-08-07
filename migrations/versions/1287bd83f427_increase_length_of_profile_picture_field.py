"""Increase length of profile_picture field

Revision ID: 1287bd83f427
Revises: 3d5433542110
Create Date: 2024-07-08 19:58:46.471653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1287bd83f427'
down_revision = '3d5433542110'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        # Custom command to alter the length of profile_picture column
        batch_op.alter_column('profile_picture',
               existing_type=sa.String(length=256),
               type_=sa.String(length=1024),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        # Custom command to revert the length of profile_picture column
        batch_op.alter_column('profile_picture',
               existing_type=sa.String(length=1024),
               type_=sa.String(length=256),
               existing_nullable=True)
    # ### end Alembic commands ###


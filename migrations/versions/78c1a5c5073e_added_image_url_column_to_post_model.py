"""Added image_url column to Post model

Revision ID: 78c1a5c5073e
Revises: 1287bd83f427
Create Date: 2024-07-08 22:17:36.194480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78c1a5c5073e'
down_revision = '1287bd83f427'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=1024), nullable=True))


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###

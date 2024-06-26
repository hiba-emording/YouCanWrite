"""Remove default value from password_hash

Revision ID: a13bbc234fb1
Revises: bb8eb9725d01
Create Date: 2024-06-18 21:58:42.505539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a13bbc234fb1'
down_revision = 'bb8eb9725d01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        # batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=False))
        pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password_hash')
    # ### end Alembic commands ###


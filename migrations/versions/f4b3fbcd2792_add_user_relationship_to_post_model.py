"""Add user relationship to Post model

Revision ID: f4b3fbcd2792
Revises: 78c1a5c5073e
Create Date: 2024-07-09 00:52:28.877857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4b3fbcd2792'
down_revision = '78c1a5c5073e'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_post_user', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint('fk_post_user', type_='foreignkey')
    # ### end Alembic commands ###


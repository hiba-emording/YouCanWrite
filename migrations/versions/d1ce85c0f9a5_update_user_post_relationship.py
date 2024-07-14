"""Update user-post relationship

Revision ID: d1ce85c0f9a5
Revises: f4b3fbcd2792
Create Date: 2024-07-09 00:59:55.665779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1ce85c0f9a5'
down_revision = 'f4b3fbcd2792'
branch_labels = None
depends_on = None


def upgrade():
    # Check if column 'user_id' exists in 'post' table before adding
    connection = op.get_bind()
    inspector = sa.inspect(connection)
    columns = inspector.get_columns('post')
    column_names = [column['name'] for column in columns]

    if 'user_id' not in column_names:
        with op.batch_alter_table('post', schema=None) as batch_op:
            batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
            batch_op.create_foreign_key('fk_post_user', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint('fk_post_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


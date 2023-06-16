"""add language to posts

Revision ID: 176d08d01ae7
Revises: 7139f238750e
Create Date: 2023-05-02 17:53:57.793578

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '176d08d01ae7'
down_revision = '7139f238750e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###
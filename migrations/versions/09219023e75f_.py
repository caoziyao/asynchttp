"""empty message

Revision ID: 09219023e75f
Revises: e1ed62d22dc4
Create Date: 2016-09-25 01:20:28.384565

"""

# revision identifiers, used by Alembic.
revision = '09219023e75f'
down_revision = 'e1ed62d22dc4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('node_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['node_id'], ['nodes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('topics')
    ### end Alembic commands ###

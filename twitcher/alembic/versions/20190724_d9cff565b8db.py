"""update service

Revision ID: d9cff565b8db
Revises: b8aa09688558
Create Date: 2019-07-24 17:10:47.137758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9cff565b8db'
down_revision = 'b8aa09688558'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_verify', sa.Integer(), nullable=True))
        batch_op.alter_column('name',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('url',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.create_index(batch_op.f('ix_services_name'), ['name'], unique=True)
        batch_op.drop_index('name_index')
        batch_op.drop_column('verify')
        batch_op.drop_column('public')

    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('verify', sa.INTEGER(), nullable=True))
        batch_op.create_index('name_index', ['name'], unique=1)
        batch_op.drop_index(batch_op.f('ix_services_name'))
        batch_op.alter_column('url',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.drop_column('_verify')

    # ### end Alembic commands ###

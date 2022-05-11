"""empty message

Revision ID: 7fd2ffff777e
Revises: 084b7a0d733b
Create Date: 2022-05-09 20:16:00.183396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fd2ffff777e'
down_revision = '084b7a0d733b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_weathers_date_del'), 'weathers', ['date_del'], unique=False)
    op.create_index(op.f('ix_weathers_timess'), 'weathers', ['timess'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_weathers_timess'), table_name='weathers')
    op.drop_index(op.f('ix_weathers_date_del'), table_name='weathers')
    # ### end Alembic commands ###
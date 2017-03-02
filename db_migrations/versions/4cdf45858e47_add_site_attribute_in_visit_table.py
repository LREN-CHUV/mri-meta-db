"""add site attribute in visit table

Revision ID: 4cdf45858e47
Revises: 927d5ceb3e86
Create Date: 2017-03-02 11:35:22.015314

"""

# revision identifiers, used by Alembic.
revision = '4cdf45858e47'
down_revision = '927d5ceb3e86'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('visit', sa.Column('site', sa.VARCHAR(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('visit', 'site')
    # ### end Alembic commands ###

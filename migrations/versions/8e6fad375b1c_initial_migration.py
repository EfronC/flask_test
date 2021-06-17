"""Initial migration.

Revision ID: 8e6fad375b1c
Revises: 
Create Date: 2021-06-16 18:21:08.581974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e6fad375b1c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ethnicity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gender',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.Text(), nullable=True),
    sa.Column('gender_id', sa.Integer(), nullable=True),
    sa.Column('ethnicity_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ethnicity_id'], ['ethnicity.id'], ),
    sa.ForeignKeyConstraint(['gender_id'], ['gender.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    op.drop_table('gender')
    op.drop_table('ethnicity')
    # ### end Alembic commands ###

"""add active_segment_description and available_segment_descriptions

Revision ID: 30a5ba9d6453
Revises: 530f0663324e
Create Date: 2024-04-05 12:02:57.843244

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "30a5ba9d6453"
down_revision = "530f0663324e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("action_event", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("active_segment_description", sa.String(), nullable=True)
        )
        batch_op.add_column(
            sa.Column("available_segment_descriptions", sa.String(), nullable=True)
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("action_event", schema=None) as batch_op:
        batch_op.drop_column("available_segment_descriptions")
        batch_op.drop_column("active_segment_description")

    # ### end Alembic commands ###
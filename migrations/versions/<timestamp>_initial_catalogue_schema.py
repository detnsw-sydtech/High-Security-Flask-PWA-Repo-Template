"""Initial catalogue schema with identifier field"""

from alembic import op
import sqlalchemy as sa


# Revision identifiers
revision = "0001_catalogue_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "item_types",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=50), nullable=False, unique=True),
    )

    op.create_table(
        "creators",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=120), nullable=False),
    )

    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=120), nullable=False),
    )

    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("description", sa.Text()),
        sa.Column("year", sa.Integer()),
        sa.Column("identifier", sa.String(length=120), unique=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("item_type_id", sa.Integer(), sa.ForeignKey("item_types.id")),
    )

    op.create_table(
        "item_creators",
        sa.Column("item_id", sa.Integer(), sa.ForeignKey("items.id"), primary_key=True),
        sa.Column("creator_id", sa.Integer(), sa.ForeignKey("creators.id"), primary_key=True),
    )

    op.create_table(
        "item_categories",
        sa.Column("item_id", sa.Integer(), sa.ForeignKey("items.id"), primary_key=True),
        sa.Column("category_id", sa.Integer(), sa.ForeignKey("categories.id"), primary_key=True),
    )


def downgrade():
    op.drop_table("item_categories")
    op.drop_table("item_creators")
    op.drop_table("items")
    op.drop_table("categories")
    op.drop_table("creators")
    op.drop_table("item_types")

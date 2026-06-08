"""add forced_locale to config tables

Revision ID: 0009
Revises: 0008
Create Date: 2026-06-03

Adds a ``forced_locale`` column to the config cascade tables. When set,
the banner uses this locale directly and skips browser-language
detection (``navigator.language``). NULL means auto-detect, preserving
the existing behaviour. Mirrors the cascade pattern of the other config
columns so the value inherits org -> group -> site.
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0009"
down_revision: str | Sequence[str] | None = "0008"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

_TABLES = ("site_configs", "site_group_configs", "org_configs")


def upgrade() -> None:
    for table in _TABLES:
        op.add_column(
            table,
            sa.Column("forced_locale", sa.String(length=10), nullable=True),
        )


def downgrade() -> None:
    for table in _TABLES:
        op.drop_column(table, "forced_locale")

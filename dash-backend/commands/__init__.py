from commands.core_provider import core_provider_cli
from commands.reindex import reindex_cli
from commands.seed import seed_cli


def init_app(app):
    app.cli.add_command(seed_cli)
    app.cli.add_command(core_provider_cli)
    app.cli.add_command(reindex_cli)

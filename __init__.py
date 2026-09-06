"""tokentelemetry plugin.

Embeds the TokenTelemetry observability dashboard (default http://localhost:3000)
inside the Hermes Dashboard so you don't need to context-switch between ports.
This __init__.py exists so the plugin directory is a proper Python package
and can be imported by the Hermes plugin loader.
"""


def register(ctx) -> None:
    """Register no runtime tools; this plugin contributes a dashboard tab only."""
    return None

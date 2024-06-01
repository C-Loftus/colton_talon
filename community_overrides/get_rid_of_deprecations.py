from talon import settings, app
from ...community.plugin.talon_draft_window import draft_talon_helpers

app.register("ready", lambda: settings.unregister("", draft_talon_helpers._update_draft_style))


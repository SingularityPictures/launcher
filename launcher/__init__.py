import sys


self = sys.modules[__name__]
self._is_installed = False


_SESSION_STEPS = (
    "AVALON_PROJECT",
    "AVALON_SILO",
    "AVALON_ASSET",
    "AVALON_TASK",
    "AVALON_APP",
)
_PLACEHOLDER = "placeholder"


def install():
    """Register actions"""

    if self._is_installed:
        return

    from . import actions

    print("Registering default actions..")
    actions.register_default_actions()
    print("Registering config actions..")
    actions.register_config_actions()
    print("Registering environment actions..")
    actions.register_environment_actions()

    self._is_installed = True

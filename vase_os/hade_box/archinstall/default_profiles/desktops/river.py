from typing import override

from archinstall.default_profiles.profile import GreeterType, Profile, ProfileType
from archinstall.tui.curses_menu import SelectMenu
from archinstall.tui.menu_item import MenuItem, MenuItemGroup
from archinstall.tui.result import ResultType
from archinstall.tui.types import Alignment, FrameProperties

class RiverProfile(Profile):
	def __init__(self) -> None:
		super().__init__(
			'River',
			ProfileType.DesktopEnv,
			packages=[],
			services=[],
			support_gfx_driver=True,
		)

	@property
	@override
	def packages(self) -> list[str]:
		return [
			'foot',
            'xorg-xwayland',
            'waybar',
            'noto-fonts',
			'noto-fonts-emoji',
			'otf-font-awesome',
            'pavucontrol',
			'xdg-desktop-portal-wlr',
			'river',
		]

	@property
	@override
	def default_greeter_type(self) -> GreeterType:
		return GreeterType.Lightdm

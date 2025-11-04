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

	@property
	@override
	def services(self) -> list[str]:
		if pref := self.custom_settings.get('seat_access', None):
			return [pref]
		return []

	def _ask_seat_access(self) -> None:
		header = 'Sway needs access to your seat (collection of hardware devices i.e. keyboard, mouse, etc)'
		header += '\n' + 'Choose an option to give Sway access to your hardware' + '\n'

		items = [MenuItem(s.value, value=s) for s in SeatAccess]
		group = MenuItemGroup(items, sort_items=True)

		default = self.custom_settings.get('seat_access', None)
		group.set_default_by_value(default)

		result = SelectMenu[SeatAccess](
			group,
			header=header,
			allow_skip=False,
			frame=FrameProperties.min('Seat access'),
			alignment=Alignment.CENTER,
		).run()

		if result.type_ == ResultType.Selection:
			self.custom_settings['seat_access'] = result.get_value().value

	@override
	def do_on_select(self) -> None:
		self._ask_seat_access()
		return None
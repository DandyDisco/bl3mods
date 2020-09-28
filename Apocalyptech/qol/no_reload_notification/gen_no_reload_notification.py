#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

import sys
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('no_reload_notification.txt',
        'No Reload Notification',
        'Apocalyptech',
        [
            "Removes the onscreen prompt to reload, when near the end of a mag.",
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='qol, ui',
        )

# Default: 0.3
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/GameplayGlobals',
        'AmmoLowPercent',
        0)

mod.close()

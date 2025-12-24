
import datetime

from Gui import Colors
from Gui import Fonts

THEME_DEFAULT = 'Default'
THEME_DARK    = 'Dark'
THEME_LIGHT   = 'Light'


class Theme:
    NAME = THEME_DEFAULT

    DashboardScreenBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardHeaderBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardHeaderBorderColor     = Colors.COLOR_VSC_TERTIARY
    DashboardBodyBackgroundColor   = Colors.COLOR_VSC_PRIMARY
    DashboardBodyBorderColor       = Colors.COLOR_VSC_TERTIARY
    DashboardFooterBackgroundColor = Colors.COLOR_VSC_PRIMARY
    DashboardFooterBorderColor     = Colors.COLOR_VSC_TERTIARY

    # DashboardReportsListSearchQueryFieldFont            = Fonts.FONT_BLENDER_PRO_BOLD
    # DashboardReportsListSearchQueryFieldFontWeight      = Fonts.Font.Bold
    # DashboardReportsListSearchQueryFieldFontSize        = 16
    # DashboardReportsListSearchQueryFieldColor           = Colors.COLOR_VSC_LIGHT
    # DashboardReportsListSearchQueryFieldBackgroundColor = Colors.COLOR_VSC_PRIMARY
    # DashboardReportsListSearchQueryFieldBorderColor     = Colors.COLOR_VSC_TERTIARY

class DarkTheme(Theme):
    NAME = THEME_DARK


class LightTheme(Theme):
    NAME = THEME_LIGHT

    DashboardScreenBackgroundColor = Colors.COLOR_WHITE
    DashboardHeaderBackgroundColor = Colors.COLOR_WHITE
    DashboardHeaderBorderColor     = Colors.COLOR_VSC_LIGHT
    DashboardBodyBackgroundColor   = Colors.COLOR_WHITE
    DashboardBodyBorderColor       = Colors.COLOR_VSC_LIGHT
    DashboardFooterBackgroundColor = Colors.COLOR_WHITE
    DashboardFooterBorderColor     = Colors.COLOR_VSC_LIGHT


CurrentTheme = None


def set_theme(theme):
    global CurrentTheme

    if theme == THEME_DARK:
        CurrentTheme = DarkTheme
        return
    
    if theme == THEME_LIGHT:
        CurrentTheme = LightTheme
        return
    
    CurrentTheme = Theme

if 6 <= datetime.datetime.now().hour < 19:
    set_theme(THEME_LIGHT)
else:
    set_theme(THEME_DARK)

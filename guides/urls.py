from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("display_settings", views.display_settings, name="display_settings"),
    path("gamebar", views.gamebar, name="gamebar"),
    path("adblock_chrome", views.adblock_chrome, name="chrome"),
    path("adblock_chrome_alt", views.adblock_chrome_alt, name="chrome_alt"),
    path("adblock_edge", views.adblock_edge, name="edge"),
    path("adblock_firefox", views.adblock_firefox, name="firefox"),
    path("battlenet_autostart", views.battlenet_autostart, name="battlenet"),
    path("epic_autostart", views.epic_autostart, name="epic"),
    path("steam_autostart", views.steam_autostart, name="steam"),
    path("apex_graphicsettings", views.apex_graphicsettings, name="apex"),
    path("fortnite_graphicsettings", views.fortnite_graphicsettings, name="fortnite"),
    path("warzone_graphicsettings", views.warzone_graphicsettings, name="warzone"),
    path("nvidia_drivers", views.nvidia_drivers, name="nvidia"),
]
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "guides/index.html")

def display_settings(request):
    return render(request, "guides/display_settings.html")

def gamebar(request):
    return render(request, "guides/gamebar.html")

def adblock_chrome(request):
    return render(request, "guides/adblock_chrome.html")

def adblock_chrome_alt(request):
    return render(request, "guides/adblock_chrome_alt.html")

def adblock_edge(request):
    return render(request, "guides/adblock_edge.html")

def adblock_firefox(request):
    return render(request, "guides/adblock_firefox.html")

def battlenet_autostart(request):
    return render(request, "guides/battlenet_autostart.html")

def epic_autostart(request):
    return render(request, "guides/epic_autostart.html")

def steam_autostart(request):
    return render(request, "guides/steam_autostart.html")

def apex_graphicsettings(request):
    return render(request, "guides/apex_graphicsettings.html")

def fortnite_graphicsettings(request):
    return render(request, "guides/fortnite_graphicsettings.html")

def warzone_graphicsettings(request):
    return render(request, "guides/warzone_graphicsettings.html")

def nvidia_drivers(request):
    return render(request, "guides/nvidia_drivers.html")
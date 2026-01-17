# orion_beer.py
# author: kudo shusanku
# date: 2026-01-15
# fun and learn
from random import choice

# Major browsers
majors = {
    "Safari",    # energy-efficient, privacy-leaning WebKit browser
    "Firefox",   # Mozilla Firefox; open-source, privacy-respecting independent browser
    "Opera",     # feature-rich, innovation-oriented Chromium browser
    "Chrome",    # Google Chrome; dominant, performance-optimized Chromium browser
    "Edge",      # Microsoft Edge; Microsoft-integrated, productivity-focused Chromium browser
}

# Zero-telemetry browsers
zero_telemetry = {
    "Orion",        # zero-telemetry, privacy-first WebKit browser
    "Brave",        # privacy-focused, ad-blocking Chromium browser
    "LibreWolf",    # hardened, telemetry-free Firefox fork
    "Tor Browser",  # anonymity-centric, onion-routed secure browser
}

# Historical browsers
historical = {
    "Nexus",                # WorldWideWeb was renamed to Nexus.
                            # The first web browser
                            # developed by Tim Berners-Lee

    "Mosaic",               # NCSA Mosaic
                            # The first widely popular graphical web browser

    "Navigator",            # Netscape Navigator
    # "Internet Explorer",  # IE (handled explicitly below)
    
    "HotJava",              # built with Java 1.0 alpha;
                            # introduced support for Java applets;
                            # developed by Sun Microsystems
}

# Minor browsers
minors = {
    "Sleipnir",   # highly customizable browser
    "Yandex",     # feature-rich, ecosystem-integrated browser
    "Vivaldi",    # ultra-customizable, power-user-oriented browser
    "Floorp",     # privacy-focused Japanese Firefox fork
}


class InternetExplorerError(Exception):
    """Raised when Internet Explorer is encountered."""
    pass


def choose_browser(name: str) -> str:
    """Classify the browser name and respond accordingly."""
    # Handle IE first to ensure the intended error is raised.
    if name == "Internet Explorer":
        raise InternetExplorerError("Unsupported browser")
    elif name in majors:
        return "Major browser"
    elif name in zero_telemetry:
        return "Zero-telemetry browser"
    elif name in minors:
        return "Minor browser"
    elif name in historical:
        return "Historical browser"
    else:
        raise ValueError(f"Unknown browser -> {name!r}")


# Union (duplicates automatically removed)
browsers = majors | zero_telemetry | historical | minors | {"Internet Explorer"}

# Deterministic display for readability/log stability
print(", ".join(sorted(browsers)))

# Random choice
yours = choice(list(browsers))
print("Today's Web browser:", yours)

# Try choosing
try:
    judge = choose_browser(yours)
except InternetExplorerError as ie:
    print(f"Please do not use this. {ie}")
except ValueError as e:
    print(f"An unexpected browser was provided: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("You may use a", judge, ".")
finally:
    print("and Orion Beer.")

"""
Browse light. Log nothing. Orion.
Then Beer.
"""


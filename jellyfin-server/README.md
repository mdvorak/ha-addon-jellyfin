# Jellyfin Server Add-on

![Supports amd64 Architecture][amd64-shield]
![Supports aarch64 Architecture][aarch64-shield]

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg

This [Home Assistant](https://www.home-assistant.io/addons/) add-on installs the
[Jellyfin](https://jellyfin.org/) server.

Server is exposed on port `8096`, and must be accessed directly.

Configuration and caches are stored on `share` (not in config), therefore
its data will not be deleted when add-on is uninstalled, and must be deleted
manually. This is intentional.

# Jellyfin Server Add-on

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg

This [Home Assistant](https://www.home-assistant.io/addons/) add-on installs the 
[Jellyfin](https://jellyfin.org/) server. It does not provide any integrations.

Server is exposed on port `8096`.

Configuration and caches are stored on `share` (not in config), therefore
its data will not be deleted when add-on is uninstalled, and must be deleted
manually. This is intentional.

_:warning: WARNING: This add-on is experimental and it was tested only on amd64._

# Jellyfin Server Add-on

This [Home Assistant](https://www.home-assistant.io/addons/) installs the actual 
[Jellyfin](https://jellyfin.org/) server. It does not provide any integrations.

Server is exposed on port `8096`.

Configuration and caches are stored on `share` (not in config), therefore
its data will not be deleted when add-on is uninstalled, and must be deleted
manually. This is intentional.

_:warning: WARNING: This add-on is experimental and it was tested only on amd64._

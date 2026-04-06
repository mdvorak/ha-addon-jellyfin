# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
FROM jellyfin/jellyfin:10.11.8

ENV JELLYFIN_DATA_DIR=/share/jellyfin
ENV JELLYFIN_CONFIG_DIR=/share/jellyfin/config
ENV JELLYFIN_CACHE_DIR=/share/jellyfin/cache
ENV JELLYFIN_LOG_DIR=/share/jellyfin/log

# Override original entrypoint
ENTRYPOINT ["./jellyfin/jellyfin"]

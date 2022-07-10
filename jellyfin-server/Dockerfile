# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

ENV JELLYFIN_DATA_DIR=/share/jellyfin
ENV JELLYFIN_CONFIG_DIR=/share/jellyfin/config
ENV JELLYFIN_CACHE_DIR=/share/jellyfin/cache

# Override original entrypoint
ENTRYPOINT ["./jellyfin/jellyfin"]

ARG HASH
FROM debian:stable-slim@${HASH}
ADD xvfb-chromium /usr/bin/xvfb-chromium
RUN apt-get update && \
    apt-get install --no-install-recommends -y xvfb chromium && \
    apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf ~/.cache && \
    rm -rf /tmp/* && \
    ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome && \
    ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser

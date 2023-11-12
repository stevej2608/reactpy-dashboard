FROM python:3.11.4-bookworm

RUN useradd -ms /bin/bash vscode

# RUN apt-get update && apt-get install -y build-essential g++ libx11-dev libxkbfile-dev libsecret-1-dev

# install chrome for scraper

RUN mkdir -p /tmp/chrome \
   && cd /tmp/chrome \
   && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN cd /tmp/chrome \
   && dpkg -i google-chrome*.deb || true \
   && apt update \
   && apt --fix-broken install -y

# Install chromedriver

RUN mkdir -p /tmp/ && \
    cd /tmp/ && \
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip  && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/bin/ && \
    # clean up the container "layer", after we are done
    rm /tmp/chromedriver.zip

# Install nodejs 20.x
# https://computingforgeeks.com/how-to-install-nodejs-on-ubuntu-debian-linux-mint/

RUN apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates && \
    curl -sL https://deb.nodesource.com/setup_20.x | bash - && \
    apt -y install nodejs

RUN npm install -g pnpm


# Mount the VSCODE project in here

RUN mkdir /workspace && \
    chown vscode:vscode /workspace

USER vscode

ENV PATH="/home/vscode/.local/bin:${PATH}"



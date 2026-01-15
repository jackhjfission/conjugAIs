#!/usr/bin/env bash

echo "Running start up script."

chmod +x /home/aprendiz/workspace/.devcontainer/on-start-host.sh && \
    /home/aprendiz/workspace/.devcontainer/on-start-host.sh

#!/bin/bash

if [[ -z "$PYPICLOUD_HOST" ]]; then
    exit 0
fi

echo "*** Configuring pypi ***"

# Upload packages - twine upload -r pypicloud dist/*

cat > ~/.pypirc <<EOF
[distutils]
index-servers =
  pypicloud

[pypicloud]
repository: http://$PYPICLOUD_HOST:6543/simple/
username: $PYPICLOUD_USER
password: $PYPICLOUD_PASSWORD
EOF

# Download packages - pip install ...
#
# https://pypicloud.readthedocs.io/en/latest/topics/getting_started.html

PIP_CONF=~/.pip/pip.conf

mkdir -p "$(dirname "$PIP_CONF")" && touch "$PIP_CONF"

cat > $PIP_CONF <<EOF
[global]
index-url = http://$PYPICLOUD_HOST:6543/simple/
trusted-host = $PYPICLOUD_HOST
EOF

# Install packages needed by vscode extensions

pip install --upgrade pip
pip install autoflake pylint

# Install some basic packages

pip install poetry invoke hatch

poetry config virtualenvs.in-project true

if [ -f  requirements.txt ]; then
    pip install -r requirements.txt
fi

# Open in poetry bash shell if it's installed and we have a .venv

FILE=/home/vscode/.bashrc
if ! grep -q poetry $FILE; then
    echo ''  >> $FILE
    echo '# Run bash in poetry shell'  >> $FILE
    echo ''  >> $FILE
    echo 'if [ -d ".venv" ] && [[ ${POETRY_ACTIVE:-"unset"} == "unset" ]]; then' >> $FILE
    echo '  poetry shell'  >> $FILE
    echo 'else'  >> $FILE
    echo '  export PS1="$ "' >> $FILE
    echo 'fi'  >> $FILE
fi

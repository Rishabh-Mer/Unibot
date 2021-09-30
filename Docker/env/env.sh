#!/bin/bash

> /usr/share/nginx/html/env_config.js
env >> .env
echo "window._env_ = {" >> /usr/share/nginx/html/env_config.js

while read -r line || [[ -n "$line" ]];
do
  if printf '%s\n' "$line" | grep -q -e '='; then
    varname=$(printf '%s\n' "$line" | sed -e 's/=.*//')
    varvalue=$(printf '%s\n' "$line" | sed -e 's/^[^=]*=//')
  fi

  value=$(printf '%s\n' "${!varname}")
  [[ -z $value ]] && value=${varvalue}

  echo "  $varname: \"$value\"," >> /usr/share/nginx/html/env_config.js
done < .env

rm .env

echo "};" >> /usr/share/nginx/html/env_config.js

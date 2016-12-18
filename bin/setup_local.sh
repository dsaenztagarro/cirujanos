MANAGE_PY_PATH=/var/www/cirujanos/manage.py
sed -i -e 's/DJANGO_SETTINGS_MODULE_VAR/<your config.settings module>/g' $MANAGE_PY_PATH
sed -i -e 's/CIRUJANOS_SECRET_KEY_VAR/<your secret key>/g' $MANAGE_PY_PATH

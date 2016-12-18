PROJECT_PATH=/var/www/cirujanos
WSGI_PATH=$PROJECT_PATH/cirujanos/wsgi.py
MANAGE_PY_PATH=$PROJECT_PATH/manage.py

SECRET_KEY="your secret key"
SETTINGS=config.settings.production

cp -f $PROJECT_PATH/examples/wsgi.py $WSGI_PATH
WSGI_PATH=/var/www/cirujanos/cirujanos/wsgi.py
sed -i -e "s/CIRUJANOS_SECRET_KEY_VAR/$SECRET_KEY/g" $WSGI_PATH
sed -i -e 's/CIRUJANOS_DB_VAR/<your DB name>/g' $WSGI_PATH
sed -i -e 's/CIRUJANOS_USER_VAR/<your DB user>/g' $WSGI_PATH
sed -i -e 's/CIRUJANOS_PASSWORD_VAR/<your DB user password>/g' $WSGI_PATH

sed -i -e "s/CIRUJANOS_SECRET_KEY_VAR/$SECRET_KEY/g" $MANAGE_PY_PATH
sed -i -e "s/DJANGO_SETTINGS_MODULE_VAR/$SETTINGS/g" $MANAGE_PY_PATH
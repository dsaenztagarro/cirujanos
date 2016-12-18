WSGI_PATH=/var/www/cirujanos/cirujanos/wsgi.py
sed -i -e 's/CIRUJANOS_SECRET_KEY_VAR/<your secret key>/g' $WSGI_PATH
sed -i -e 's/CIRUJANOS_DB_VAR/<your DB name>/g' $WSGI_PATH
sed -i -e 's/CIRUJANOS_USER_VAR/<your DB user>/g' $WSGI_PATH
sed -i -e 's/CIRUJANOS_PASSWORD_VAR/<your DB user password>/g' $WSGI_PATH

sed -i -e 's/DJANGO_SETTINGS_MODULE_VAR/<your config.settings modules>/g' $WSGI_PATH
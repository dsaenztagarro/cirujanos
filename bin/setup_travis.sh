PROJECT_PATH=/home/travis/build/dsaenztagarro/cirujanos
WSGI_PATH=$PROJECT_PATH/cirujanos/wsgi.py
MANAGE_PY_PATH=$PROJECT_PATH/manage.py

SECRET_KEY=2b9afb89a6acc1575b159bfca38d10ad
SETTINGS=config.settings.travis

cp -f $PROJECT_PATH/cirujanos/wsgi.py.example $WSGI_PATH

sed -i -e "s/CIRUJANOS_SECRET_KEY_VAR/$SECRET_KEY/g" $WSGI_PATH
sed -i -e 's/CIRUJANOS_DB_VAR/cirujanos_development/g' $WSGI_PATH
sed -i -e 's/CIRUJANOS_USER_VAR/root/g' $WSGI_PATH
sed -i -e 's/CIRUJANOS_PASSWORD_VAR//g' $WSGI_PATH
sed -i -e "s/DJANGO_SETTINGS_MODULE_VAR/$SETTINGS/g" $WSGI_PATH

cp -f $PROJECT_PATH/manage.py.example $PROJECT_PATH/manage.py

sed -i -e "s/CIRUJANOS_SECRET_KEY_VAR/$SECRET_KEY/g" $MANAGE_PY_PATH
sed -i -e "s/DJANGO_SETTINGS_MODULE_VAR/$SETTINGS/g" $MANAGE_PY_PATH

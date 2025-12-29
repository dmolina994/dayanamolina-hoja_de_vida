#!/usr/bin/env bash
# Salir si ocurre un error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recopilar archivos estáticos
python manage.py collectstatic --no-input

# Aplicar migraciones
python manage.py migrate

# Crear superusuario automáticamente si no existe
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'dayanamolinaQgmail.com', '123')
    print('Usuario creado')
else:
    print('El usuario ya existe')
EOF
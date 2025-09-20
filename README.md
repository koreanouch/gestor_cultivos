Gestor de Cultivos (Django)

Aplicación de ejemplo para gestionar huertos urbanos: permite crear, listar, editar y eliminar cultivos asociados a sectores del huerto, registrando estado y fecha de siembra.
Características

    CRUD completo de Cultivos con vistas genéricas (ListView, CreateView, UpdateView, DeleteView).

    Relación Sector → Cultivo mediante ForeignKey y conteo de cultivos por sector.

    Estados del cultivo con choices: Semilla, En Crecimiento, Listo para Cosechar.

    Plantillas con Bootstrap 5 y estructura recomendada de templates.

Requisitos

    Python 3.10+

    Django 4/5

    Pip y virtualenv recomendados

Instalación

    Clonar el repositorio

    git clone https://github.com/koreanouch/gestor_cultivos.git

    cd gestor_cultivos

    Crear entorno y dependencias

    python -m venv .venv

    Activar:

        Windows: .venv\Scripts\activate

        macOS/Linux: source .venv/bin/activate

    pip install -r requirements.txt

        Si no existe, al menos: pip install django

    Migraciones y superusuario

    python manage.py makemigrations

    python manage.py migrate

    python manage.py createsuperuser

    Ejecutar servidor

    python manage.py runserver
    Abrir http://127.0.0.1:8000/

Estructura principal

    proyecto_huerto/: settings y urls del proyecto

    gestion_huerto/: modelos, vistas, urls y templates de la app

    templates/base.html: layout con Bootstrap 5

    db.sqlite3: base local por defecto

Modelos

    Sector(nombre)

    Cultivo(nombre, fecha_siembra, estado, sector)

        unique_together en (nombre, sector)

        estados: semilla | crecimiento | cosecha

Rutas

    / → Lista de cultivos

    /nuevo/ → Crear cultivo

    /<id>/editar/ → Editar cultivo

    /<id>/eliminar/ → Eliminar cultivo

Bootstrap 5 (CDN)

En base.html se incluyen los enlaces a CSS/JS de Bootstrap 5 para estilos rápidos.
Datos iniciales (opcional)

Vía Admin

    Ir a /admin, crear Sectores (Balcón, Patio, Invernadero) y luego Cultivos.

Vía Shell

    python manage.py shell

    from gestion_huerto.models import Sector, Cultivo

    Crear sectores: Sector.objects.bulk_create([Sector(nombre="Balcón"), Sector(nombre="Patio"), Sector(nombre="Invernadero")])

Configuración regional

    LANGUAGE_CODE = 'es-cl'

    TIME_ZONE = 'America/Santiago'

    Formato de entrada para DateField por defecto: YYYY-MM-DD.

Scripts útiles

    Formateo y checks: agregar según tu flujo (flake8, black, isort, etc.).

    Correr servidor: python manage.py runserver

    Migraciones: python manage.py makemigrations && python manage.py migrate

Contribuir

    Crear rama feature/nombre

    Hacer PR con descripción breve de cambios y capturas si aplica.

Licencia

    MIT (ajusta si necesitas otra).

Autor

    koreanouch (Víctor)

Para publicar cambios:

    git add .

    git commit -m "Descripción"

    git push

from setuptools import setup, find_packages

setup(
    name="django-facile-cli",
    version="1.0.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
         "django>=4.2",
         "python-dotenv>=1.0",
         "psycopg2-binary",
    ],
    entry_points={
        "console_scripts": [
          "django-facile=django_facile.cli:main"
        ]
    },
    author="Yogeswar",
    description="Production-ready Django project generator CLI",
)
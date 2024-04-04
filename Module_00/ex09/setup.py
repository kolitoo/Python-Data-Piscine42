from setuptools import setup, find_packages

setup(
    name='ft_package',  # Utiliser des tirets au lieu de underscores pour le nom
    version='0.0.1',
    summary="Un package pour compter les occurrences dans une liste",
    home_page="https://github.com/abourdon/ft-package",  # Ajoutez l'URL de la page d'accueil de votre package
    author='abourdon',
    author_email="abourdon@42.fr",
    license="MIT",
    location="/opt/homebrew/lib/python3.11/site-packages",
    requires="",  # Laisser vide pour le moment
    required_by="",  # Laisser vide pour le moment
    metadata_version="2.1",
    installer="pip",
    classifiers=[],  # Assurez-vous de remplir cette liste avec les classifiers appropriés
    entry_points={},  # Laisser vide pour le moment
    packages=find_packages(),
    description='Un package pour compter les occurrences dans une liste',
)
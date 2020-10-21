from setuptools import setup
setup(
    name = 'digibeectl',
    version = '0.1.0',
    packages = ['digibeectl'],
    entry_points = {
        'console_scripts': [
            'digibeectl = digibeectl.__main__:main'
        ]
    })
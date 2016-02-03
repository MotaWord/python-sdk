from setuptools import setup

setup(
    name='motaword',
    packages=['motaword_sdk'],
    version='0.9.0',
    description='Motaword Python SDK',
    long_description='Use MotaWord API to post '
                     'and track your translation projects.',
    url='https://www.motaword.com/developer',
    author='Sergey Tikhonov',
    author_email='srg.tikhonov@gmail.com',
    license='MIT',
    install_requires=[
        'requests>=2',
    ]
)

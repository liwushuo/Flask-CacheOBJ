"""
Flask-Cache provides some caching decorators
"""

from setuptools import setup


setup(
    name='Flask-Cache',
    version='0.0.1',
    url='https://ghe.liwushuo.com/flask-extensions/Flask-Cache',
    license='MIT',
    author='Ju Lin',
    author_email='soasme@gmail.com',
    description='Flask-Cache provides some caching decorators',
    long_description=__doc__,
    packages=['flask_cache'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'python-dateutil',
        'pytz',
        'msgpack-python',
        'redis',
    ],
    classifiers=[
        'Framework :: Flask',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

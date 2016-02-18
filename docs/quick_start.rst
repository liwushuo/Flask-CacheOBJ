Quick Start
===========

Installation
------------

Install the extension with one of the following commands::

    $ easy_install Flask-CacheOBJ

or alternatively if you have pip installed::

    $ pip install Flask-CacheOBJ

Initialize CacheOBJ
-------------------

Cache is managed through a ``FlaskCacheOBJ`` instance::

    from flask import Flask
    from flask.ext.cacheobj import FlaskCacheOBJ

    app = Flask(__name__)
    cache = FlaskCacheOBJ(app)

You may also set up your ``FlaskCacheOBJ`` instance later at configuration time using
**init_app** method::

    cache = FlaskCacheOBJ()

    app = Flask(__name__)
    cache.init_app(app)

Configuration
-------------

The following configuration values exist for Flask-CacheOBJ:

.. tabularcolumns:: |p{6.5cm}|p{8.5cm}|

=================== ====================================================================
``CACHE_HOST``      A Redis server host.
``CACHE_PORT``      A Redis server port. Default is 6379.
``CACHE_DB``        A Redis db (zero-based number index). Default is 0.
``CACHE_PREFIX``    Prefix attached before your key definition. Default is empty string.
=================== ====================================================================

Define Cache Strategy
---------------------

Each strategy is a dict contains `key`, `expire` if possible::

    ITEM = {
        'key': 'item:{item_id}',
        'expire': 86400
    }
    ITEM_STAT = {
        'key': 'item_stat:{item_id}',
        'expire': 86400
    }
    ITEM_LIST = {
        'key': 'item_list:{item_list_id}',
        'expire': 86400
    }
    ITEM_HASH = {
        'key': '{item_id}',
        'expire': 86400
    }

Cache Object
------------

To cache object you will use the `cache.obj` decorator::

    @cache.obj(ITEM)
    def get_item(item_id):
        return to_dict(Item.query.get(item_id))

Cache Counter
-------------

To cache counter you will use the `cache.counter` decorator::

    @cache.counter(ITEM_STAT)
    def get_item_stat(item_id):
        return to_dict(ItemStat.query.get(item_id))

Cache List
----------

To cache list you will use the `cache.list` decorator::

    @cache.counter(ITEM_LIST)
    def get_item_list(item_list_id):
        return map(to_dict, ItemList.query.filter_by(item_list_id=item_list_id).all())

Cache Hash
----------

To cache hash you will use the `cache.hash` decorator::

    @cache.counter(ITEM_HASH)
    def get_item(item_id):
        return to_dict(Item.query.get(item_id))

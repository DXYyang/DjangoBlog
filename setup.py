# coding:utf-8
from setuptools import setup, find_packages

setup(
    name='BologWeb',
    version='${version}',
    description='Blog System base on Django',
    author='xuyang',
    author_email='',
    url='',
    license='MIT',
    packages=find_packages('BlogWeb'),  # 在指定目录下寻找所有Python包（含有__init__.py的文件夹）
    package_dir={'': 'BlogWeb'},  # 定义指定目录,从setup的同级目录下开始配
    include_package_data=True,
    install_requires=[
        'django~=2.0',
        'gunicorn==19.8.1',
        'supervisor==4.0.0dev0',
        'xadmin==2.0.1',
        'mysqlclient==1.3.12',
        'django-ckeditor==5.4.0',
        'django-rest-framework==0.1.0',
        'django-redis==4.8.0',
        'django-autocomplete-light==3.2.10',
        'mistune==0.8.3',
        'Pillow==8.2.0',
        'coreapi==2.3.3',
        'django-redis==4.8.0',
        'hiredis==0.2.0',
        # debug
        'django-debug-toolbar==1.9.1',
        'django-silk==2.0.0',
    ],
    scripts=[
        'BlogWeb/manage.py',
        'BlogWeb/BlogWeb.wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'blogweb_manage=manage:main',
        ]
    },
    classifiers=[
        'Development Status::3-Alpha',
        'Intended Audience::Developers',
        'Topic::Blog::Django Blog',
        'License::OSI Approved::MIT License',
        'Programming Language::Python::3.6'
    ]
)

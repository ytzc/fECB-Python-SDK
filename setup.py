from setuptools import setup, find_packages



version = '0.0.1'
description = 'fECB-Python-SDK for File, HC Service, Device Service'


setup(
    name="fECB-Python-SDK",
    version=version,
    author="Jerry Yang",
    author_email="jerry.yang@fiduciaedge.com",
    description=description,
    packages=find_packages,
    #include_package_data=True,   # 启用清单文件MANIFEST.in
    #exclude_package_date={'':['.gitignore']},
    install_requires=[          # 依赖列表
        'Python>=3.6',
    ]
)
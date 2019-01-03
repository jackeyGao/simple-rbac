from setuptools import setup

with open('README.rst') as readme:
    next(readme)
    long_description = ''.join(readme).strip()

setup(
    name='simplerbac',
    version='0.1.2',
    description='as is simple-rbac.',
    long_description=long_description,
    keywords='rbac permission acl access-control',
    author='Jiangge Zhang',
    author_email='tonyseek@gmail.com',
    url='https://github.com/jackeyGao/simple-rbac',
    license='MIT License',
    packages=['rbac'],
    zip_safe=False,
    platforms=['Any'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

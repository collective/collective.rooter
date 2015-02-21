from setuptools import find_packages
from setuptools import setup

version = '1.0.dev0'

setup(
    name='collective.rooter',
    version=version,
    description=u"Tools to force catalog queries to obey the current "
                u"navigation root",
    long_description="%s\n%s" % (
        open("README.rst").read(),
        open("CHANGES.rst").read()
    ),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plone navigation root',
    author='Martin Aspeli',
    author_email='optilude@gmail.com',
    url='http://pypi.python.org/pypi/collective.rooter',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'collective.monkeypatcher',
    ],
    extras_require=dict(
        test=[
            'Products.PloneTestCase',
        ],
    ),
    entry_points="""
      """,
)

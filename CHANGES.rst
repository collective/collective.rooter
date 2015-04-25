Changelog
=========

1.0 (unreleased)
----------------

- Patch ``plone.app.uuid.utils.uuidToCatalogBrain`` to search from the portal
  root path instead of ``INavigationRoot`` path. This allows to find content
  from other subsites via the UUID. Objects are still secured by permission
  checks.
  [thet]

- PEP 8.
  [thet]


1.0b1 (2009-03-29)
------------------

- Initial release.
  [optilude]

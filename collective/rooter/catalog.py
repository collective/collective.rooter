from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.CatalogTool import CatalogTool
from collective.rooter.navroot import getNavigationRoot
from plone.app.uuid import utils
import plone.api


# Make portal_catalog's search function use a navigation root if no path
# parameter is given
CatalogTool._oldSearchResults = CatalogTool.searchResults


def searchResults(self, REQUEST=None, **kw):
    if 'path' not in kw and (REQUEST is None or 'path' not in REQUEST):
        root = getNavigationRoot()
        if root is not None:
            kw = kw.copy()
            kw['path'] = '/'.join(root.getPhysicalPath())
    return CatalogTool._oldSearchResults(self, REQUEST, **kw)


# Patch plone.app.uuid's uuidToCatalogBrain to not be rooted to INavigationRoot
# like searchResults above. Allow to retrieve the object, if the UUID is known.
# Objects are still secured by permission checks.
_oldUuidToCatalogBrain = utils.uuidToCatalogBrain


def uuidToCatalogBrain(uuid):
    portal = plone.api.portal.get()
    if portal is None:
        return None

    catalog = getToolByName(portal, 'portal_catalog', None)
    if catalog is None:
        return None

    result = catalog(UID=uuid, path=portal.getPhysicalPath())
    if len(result) != 1:
        return None

    return result[0]

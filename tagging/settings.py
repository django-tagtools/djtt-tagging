"""
Convenience module for access of custom tagging application settings,
which enforces default settings when the main settings module does not
contain the appropriate settings.

"""
from django.conf import settings


#
# The maximum length of a tag's name.
#
MAX_TAG_LENGTH = getattr(settings, 'MAX_TAG_LENGTH', 50)

#
# Whether or not tage case should be normalized. Supported values are either
# False or one of the method names in utils.TagNameNormalizer (i.e. upper_case,
# lower_case, and capwords).
#
# Backwards compatibility is provided for the old FORCE_LOWERCASE_TAGS
# configuration option.
#
if hasattr(settings, 'FORCE_LOWERCASE_TAGS') and settings.FORCE_LOWERCASE_TAGS:
    NORMALIZE_TAG_CASE = 'lower_case'
else:
    NORMALIZE_TAG_CASE = getattr(settings, 'NORMALIZE_TAG_CASE', False)
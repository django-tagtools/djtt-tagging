=======================
Django TagTools Tagging
=======================

This is a generic tagging application for Django projects, originally based
off of brosner/django-tagging which is no longer maintained. Our intent is
to maintain an upgrade path from django-tagging through the use of South
migrations.

In an effort to help keep a Django tagging project moving forward and not
stagnate like many others, this project has been put under a GitHub "organization".
The idea being that if the current maintainers no longer can maintain it, that
the baton can be easily passed on to someone else.

For installation instructions, see the file "INSTALL.txt" in this directory; for
instructions on how to use this application, and on what it provides, see the
file "overview.txt" in the "docs/" directory.

What Is New
===========

The following is a summary of what has changed since forking from django-tagging:

* Support has been dropped for legacy Django. This works on Django 1.3+,
anything less than that is not being tested.

* Tag name normalization has been added. You can now specify via a setting that
all tags be stored as upper-case, lower-case, or capitalized regardless of how
the user enters them in. A Django managment function has been added to normalize
all tags based on your current setting.

* Basic synonym support has been added. Tags can now have a series of synonyms
attached to them. Any time a synonym is used when adding a tag to a piece of
content, it will be replaced with the tag when the object is saved.

* Tags now have a display name. If you want to override the display of a tags
name, fill in the display name in the tag admin. The Tag model now has a
get_display_name method which will get the display name (if it exists) or the
regular tag name otherwise.

Contributors
============

Sponsorship for the Django TagTools project has been provided by:
    Ground Truth Trekking (http://www.groundtruthtrekking.org)

Based on the original code, written by:
    Jonathan Buchanan <jonathan.buchanan@gmail.com>

Enhanced by:
    Damien Tougas (http://www.outsideways.com) <damien@tougas.net>
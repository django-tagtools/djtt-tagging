from django.contrib import admin
from tagging.models import Tag, TaggedItem, Synonym
from tagging.forms import TagAdminForm

class SynonymInline(admin.TabularInline):
    model = Synonym

class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm
    inlines = [SynonymInline,]

admin.site.register(TaggedItem)
admin.site.register(Tag, TagAdmin)





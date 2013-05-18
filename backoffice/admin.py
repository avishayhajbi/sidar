# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from imagekit.admin import AdminThumbnail
from modeltranslation.admin import TranslationAdmin

import models
from django.contrib.auth.admin import UserAdmin


regular_models = [models.Generation]
TranslationAdmin.actions_on_bottom = True
TranslationAdmin.actions_on_top = False
TranslationAdmin.ordering = ('name_he',)


class TranslatedModelAdmin(TranslationAdmin):
    # search_fields = ['name_he']
    list_display = ('name_he', 'name_en')
    ordering = ('name_he',)


class DisciplineAdmin(TranslationAdmin):
    list_display = ('name_he', 'name_en', 'active', 'work_count')


class WorkAdmin(TranslationAdmin):
    admin_thumbnail = AdminThumbnail(image_field='processed_image')
    admin_thumbnail.short_description = u'תצוגה מקדימה'
    list_display = ('sidar_id', 'name', 'designer', 'category', 'discipline', 'admin_thumbnail')
    ordering = ('-id',)
    list_filter = ('discipline', 'category', 'designer', 'of_collections')
    filter_horizontal = ['subjects']

    def queryset(self, request):
        qs = super(WorkAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(designer=request.user.get_profile().in_charge_of_designers.all())


class DesignerAdmin(TranslationAdmin):
    list_display = ('name', 'main_discipline', 'generation', 'birth_year', 'is_active', 'show_work_count', )
    list_filter = ('generation', 'is_active')
    ordering = ['-work__count']

    def queryset(self, request):
        return models.Designer.objects.with_counts()

    def show_work_count(self, instance):
        return instance.work__count
    show_work_count.admin_order_field = 'work__count'
    show_work_count.short_description = u'מספר עבודות'


class CollectorAdmin(TranslationAdmin):
    list_display = ('name',)


class UserProfileInline(admin.StackedInline):
    model = models.UserProfile


class UserAdmin(UserAdmin):
    search_fields = ()
    list_filter = ()
    inlines = (UserProfileInline, )
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'get_designers')

    def get_designers(self, instance):
        names = [item.name for item in instance.get_profile().in_charge_of_designers.all()]
        return ', '.join(names)
    get_designers.short_description = u'מעצבים בטיפול'


class CategorySubjectModelAdmin(TranslationAdmin):
    list_display = ['name', 'parent', 'main_discipline', 'info']
    list_filter = ['parent']

admin.site.register(models.Category, CategorySubjectModelAdmin)
admin.site.register(models.Subject, CategorySubjectModelAdmin)
admin.site.register(models.Work, WorkAdmin)
admin.site.register(models.Designer, DesignerAdmin)
admin.site.register(models.Discipline, DisciplineAdmin)
admin.site.register(models.Collector, CollectorAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

for model in regular_models:
    admin.site.register(model, TranslatedModelAdmin)

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTags


class ArticleTagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
                continue
        if count > 1:
            raise ValidationError('Выберите 1 основной тэг')
        return super().clean()


class ArticleTagsInline(admin.TabularInline):
    model = ArticleTags
    extra = 3
    formset = ArticleTagsInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagsInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

# user admin  pasword admin
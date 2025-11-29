from modeltranslation.translator import register, TranslationOptions
from .models import Product, Category, Brand

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('name',)

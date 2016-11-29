from django.utils import translation

class TranslatedField(object):
    def __init__(self, en_field, es_field, pua_field):
        self.en_field = en_field
        self.es_field = es_field
        self.pua_field = pua_field

    def __get__(self, instance, owner):
        if translation.get_language() == 'es':
            return getattr(instance, self.es_field)
        elif translation.get_language() == 'pua':
            return getattr(instance, self.pua_field)
        else:
            return getattr(instance, self.en_field)

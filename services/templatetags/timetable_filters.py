from django import template
register = template.Library()


@register.filter
def get_subject(dictionary, key):
    return dictionary.get(key)[0]

@register.filter
def get_room(dictionary, key):
    return dictionary.get(key)[1]


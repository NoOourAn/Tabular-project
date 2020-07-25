from django import template
register = template.Library()


@register.filter
def get_subject(dictionary, key):
    # if dictionary.get(key)[0+6]:
    if len(dictionary.get(key))>6:
        return dictionary.get(key)[0]+' | '+dictionary.get(key)[0+3]+' | '+dictionary.get(key)[0+6]
    elif len(dictionary.get(key))>3:
        return dictionary.get(key)[0]+' | '+dictionary.get(key)[0+3]
    else:
        return dictionary.get(key)[0]

@register.filter
def get_room(dictionary, key):
    if len(dictionary.get(key))>6:
        return dictionary.get(key)[1]+' | '+dictionary.get(key)[1+3]+' | '+dictionary.get(key)[1+6]
    elif len(dictionary.get(key))>3:
        return dictionary.get(key)[1]+' | '+dictionary.get(key)[1+3]
    else:
        return dictionary.get(key)[1]

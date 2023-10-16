from django import template
from test1.models import Personality
import json

register = template.Library()

@register.filter
def index(sequence, position):
    return sequence[position]

@register.filter
def get_symbols(s):
    s = json.loads(s)
    d = s['d']
    return d.keys()

@register.filter
def get_careers_by_symbol(symbol, personality_text):
    p = Personality.objects.get(personality_text=personality_text)
    s = json.loads(p.personality_careers_by_symbol)
    d = s['d']
    return '-'.join(d[symbol])
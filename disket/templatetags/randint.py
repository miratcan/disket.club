import random
from django import template

register = template.Library()

class RandintNode(template.Node):
    def __init__(self, var_name, a, b):
        self.var_name = var_name
        self.a = template.Variable(a)
        self.b = template.Variable(b)

    def render(self, context):
        a = self.a.resolve(context)
        b = self.b.resolve(context)
        context[self.var_name] = random.randint(a, b)
        return ''

@register.tag
def randint(parser, token):
    try:
        tag_name, var_name, a, b = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires exactly three arguments" % token.contents.split()[0]
        )
    return RandintNode(var_name, a, b)


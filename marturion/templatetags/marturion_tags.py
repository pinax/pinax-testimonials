from django import template

from marturion.models import Testimoninal


register = template.Library()


class TestimonialsNode(template.Node):
    
    @classmethod
    def handle_token(cls, parser, token, order_by, **kwargs):
        bits = token.split_contents()
        
        if len(bits) != 3:
            raise template.TemplateSyntaxError("%r takes exactly two arguments "
                "(first argument must be 'as')" % bits[0])
        if bits[1] != "as":
            raise template.TemplateSyntaxError("Second argument to %r must be "
                "'as'" % bits[0])
        
        return cls(bits[2], order_by)
    
    def __init__(self, context_var, order_by):
        self.context_var = context_var
        self.order_by = order_by
    
    def render(self, context):
        context[self.context_var] = Testimoninal.objects.filter(
            active=True
        ).order_by(
            self.order_by
        )
        return u""


@register.tag
def random_testimonials(parser, token):
    return TestimonialsNode.handle_token(parser, token, order_by="?")


@register.tag
def testimonials(parser, token):
    return TestimonialsNode.handle_token(parser, token, order_by="-added")

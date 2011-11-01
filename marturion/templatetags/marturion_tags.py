from django import template

from marturion.models import Testimonial


register = template.Library()


class TestimonialsNode(template.Node):
    
    @classmethod
    def handle_token(cls, parser, token, order_by, **kwargs):
        bits = token.split_contents()
        
        if len(bits) != 4:
            raise template.TemplateSyntaxError("%r takes exactly three arguments "
                "(second argument must be 'as')" % bits[0])
        if bits[2] != "as":
            raise template.TemplateSyntaxError("Second argument to %r must be "
                "'as'" % bits[0])
        
        return cls(parser.compile_filter(bits[1]), bits[3], order_by)
    
    def __init__(self, how_many, context_var, order_by):
        self.how_many = how_many
        self.context_var = context_var
        self.order_by = order_by
    
    def render(self, context):
        how_many = self.how_many.resolve(context)
        context[self.context_var] = list(Testimonial.objects.filter(
                active=True
            ).order_by(
                self.order_by
            )[:how_many]
        )
        return u""


@register.tag
def random_testimonials(parser, token):
    return TestimonialsNode.handle_token(parser, token, order_by="?")


@register.tag
def testimonials(parser, token):
    return TestimonialsNode.handle_token(parser, token, order_by="-added")

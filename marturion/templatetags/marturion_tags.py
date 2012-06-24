from django import template

from marturion.models import Testimonial


register = template.Library()


class TestimonialsNode(template.Node):
    
    @classmethod
    def handle_token(cls, parser, token, order_by, **kwargs):
        bits = token.split_contents()
        if len(bits) == 3:
            if bits[1] != "as":
                raise template.TemplateSyntaxError("Second argument to %r must be 'as'" % bits[0])
            return cls(1, bits[2], order_by)
        elif len(bits) == 4:
            if bits[2] != "as":
                raise template.TemplateSyntaxError("Second argument to %r must be 'as'" % bits[0])
            return cls(parser.compile_filter(bits[1]), bits[3], order_by)
        else:
            raise template.TemplateSyntaxError("Invalid number of arguments for %r " % bits[0])
    
    def __init__(self, how_many, context_var, order_by):
        self.how_many = how_many
        self.context_var = context_var
        self.order_by = order_by
    
    def render(self, context):
        if self.how_many == 1:
            how_many = 1
        else:
            how_many = self.how_many.resolve(context)
        context[self.context_var] = list(Testimonial.objects.filter(
                active=True
            ).order_by(
                self.order_by
            )[:how_many]
        )
        if how_many == 1:
            context[self.context_var] = context[self.context_var][0]
        return u""


@register.tag
def random_testimonials(parser, token):
    return TestimonialsNode.handle_token(parser, token, order_by="?")


@register.tag
def random_testimonial(parser, token):
    return TestimonialsNode.handle_token(parser, token, order_by="?")


@register.tag
def testimonials(parser, token):
    return TestimonialsNode.handle_token(parser, token, order_by="-added")

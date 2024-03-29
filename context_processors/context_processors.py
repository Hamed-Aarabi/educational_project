from course.models import Tag
from blog.models import BlogTag
from cart.cart_module import Cart
from contactus.models import ContactWay, ContactSocial


def get_tags_course(request):
    tags = Tag.objects.all()
    return {'tags': tags}


def get_tags_blog(request):
    blog_tags = BlogTag.objects.all()
    return {'blog_tags': blog_tags}


def cart_item(request):
    cart = Cart(request)
    return {'cart': cart}


def contactus_way(request):
    ways = ContactWay.objects.last()
    socials = ContactSocial.objects.all()
    return {'ways': ways, 'socials': socials}

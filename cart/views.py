from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from course.models import Course
from .cart_module import Cart
from .models import *


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart.html', {'cart': cart})


class AddToCartView(View):
    def get(self, request, slug):
        course = get_object_or_404(Course, slug=slug)
        cart = Cart(request)
        cart.add(course)
        return redirect('cart:detail')


class RemoveFromCartView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.remove(id)
        return redirect('cart:detail')


class OrderCreateView(View):
    def get(self, request):
        cart = Cart(request)
        if cart.cart_len() > 0:
            order = Order.objects.create(user=request.user, final_price=cart.total())

            for item in cart:
                OrderItem.objects.create(order=order, name=item['name'], quantity=item['quantity'], image=item['image'],
                                         price=item['price'])
                course = Course.objects.get(title=item['name'])
                course.student.add(order.user)
                course.save()
            cart.delete()
            return redirect('home')
        else:
            cart.delete()
            return redirect('course:all')

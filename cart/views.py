from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from course.models import Course
from .cart_module import Cart
from .models import *
from .mixins import MyLoginRequiredMixin


class CartDetailView(MyLoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart.html', {'cart': cart})


class AddToCartView(MyLoginRequiredMixin, View):
    def get(self, request, slug):
        course = get_object_or_404(Course, slug=slug)
        if course.is_free:
            course.student.add(request.user)
            return redirect('course:detail', course.slug)
        if course.is_discount:
            course.price = course.price - int((course.price * course.discount_percentage) / 100)
        cart = Cart(request)
        cart.add(course)
        return redirect('cart:detail')


class RemoveFromCartView(MyLoginRequiredMixin, View):
    def get(self, request, id):
        cart = Cart(request)
        cart.remove(id)
        return redirect('cart:detail')


class OrderCreateView(MyLoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        if cart.cart_len() > 0:
            order = Order.objects.create(user=request.user, final_price=cart.total())
            for item in cart:
                OrderItem.objects.create(order=order, name=item['name'], quantity=item['quantity'], image=item['image'],
                                         price=item['price'])
            cart.delete()
            return redirect('cart:order-payment', order.id)
        else:
            cart.delete()
            return redirect('course:all')


class PaymentView(View):
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        if order.is_paid:
            return redirect('home')
        return render(request, 'cart/payment.html', {'order': order})

    def post(self, request, pk):
        order = Order.objects.get(id=pk)
        for item in order.order_item.all():
            course = Course.objects.get(title=item.name)
            course.student.add(Order.objects.get(id=pk).user)
            course.save()
        order.is_paid = True
        order.save()
        return redirect('home')

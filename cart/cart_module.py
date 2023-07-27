from django.shortcuts import get_object_or_404
from course.models import Course

CART_SESSION_ID = 'cart'  # key of cart in sessions dictionary


class Cart:
    def __init__(self, request):
        self.session = request.session  # create session
        cart = self.session.get(CART_SESSION_ID)  # get session with key cart in sessions dictionary
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            item['course'] = get_object_or_404(Course, id=int(item['id']))
            item['total_price'] = int(item['price']) * int(item['quantity'])
            item['unique'] = self.unique_id_generator(item['id'], item['name'])
            yield item

    def unique_id_generator(self, id, name):
        result = f'{id}-{name}'
        return result

    def add(self, course):
        unique_id = self.unique_id_generator(course.id, course.title)
        if unique_id in self.cart:
            return self.cart[unique_id]
        self.cart[unique_id] = {'name': course.title, 'image': course.image.url, 'price': str(course.price),
                                'id': str(course.id), 'quantity': 1}
        self.save()

    def total(self):
        cart = self.cart.copy()
        total = 0
        total = sum(int(item['price']) * int(item['quantity']) for item in cart.values())
        return total

    def remove(self, id):
        if id in self.cart:
            self.cart[id]['quantity'] -= 1
            if self.cart[id]['quantity'] == 0:
                del self.cart[id]  # del is for delete a key from dictionary
            self.save()

    def save(self):
        self.session.modified = True

    def delete(self):
        del self.session[CART_SESSION_ID]

    def cart_len(self):
        return len(self.cart)

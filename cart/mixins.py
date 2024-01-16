from django.shortcuts import redirect


class MyLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login')
        return super(MyLoginRequiredMixin, self).dispatch(request, *args, **kwargs)

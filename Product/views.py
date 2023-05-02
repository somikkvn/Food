# import necessary views and models from Django
from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Product, Order, Ingredient
from .forms import OrderForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# create a ProductListView class that inherits from Django's ListView
class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_set = Product.objects.all()

        if self.kwargs.get('category'):
            category = self.kwargs.get('category')
            if (category == 1):
                filter_set = filter_set.filter(category="Перші страви")
            elif (category == 2):
              filter_set = filter_set.filter(category="Другі страви")
            elif (category == 4):
              filter_set = filter_set.filter(category="Напої")
            elif (category == 5):
              filter_set = filter_set.filter(category="Десерт")

        context["products"] = filter_set
        # And so on for more models
        return context

# create a ProductDetailView class that inherits from Django's DetailView
class ProductDetailView(DetailView):
    model = Product

    # override get_context_data method to add extra context to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = kwargs['object'].ingredient.all() # add related ingredients to the context
        return context

# create an OrderListView class that inherits from Django's ListView and requires login
@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order

    # override get_queryset method to show only orders made by the logged in user
    def get_queryset(self):
        return Order.objects.filter(order_by=self.request.user)

# create an OrderCreateView class that inherits from Django's CreateView and requires login
@method_decorator(login_required, name='dispatch')
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = '/order/conformed/'

    # override get_context_data method to add extra context to the template
    def get_context_data(self,  object_list=None, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, slug=self.kwargs['slug']) # get the selected product
        context['item'] = 'item'
        return context

    # override form_valid method to set product and cost values based on form input
    def form_valid(self, form):
        slug = self.kwargs.get('slug')
        product = Product.objects.get(slug__iexact=slug)
        form.instance.product = product
        form.instance.cost = int(form.instance.count)* (int(product.price))

        return super(OrderCreateView, self).form_valid(form)

# create an OrderDetailView class that inherits from Django's DetailView and requires login
@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order

# create a function to render a "thank you" page after an order is confirmed
def order_conform(self):
    return render(self, 'Product/thanks.html')

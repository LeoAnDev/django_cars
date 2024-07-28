"""
cars/views.py
"""

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from cars.models import Car
from cars.forms import CarModelForm


class CarListView(ListView):
    """
    Exibe uma lista de carros
    """

    model = Car
    template_name = "car_list.html"
    context_object_name = "cars"
    paginate_by = 10

    def get_queryset(self):
        """
        Lista os carros em ordem de modelo, com busca
        """
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(model__icontains=search)
        return queryset.order_by("model")


@method_decorator(login_required(login_url="login"), name="dispatch")
class NewCarCreateView(CreateView):
    """
    Cria um novo carro
    """

    model = Car
    form_class = CarModelForm
    template_name = "car_new.html"
    success_url = reverse_lazy("cars_list")


class CarDetailView(DetailView):
    """
    Exibe os detalhes de um carro
    """

    model = Car
    template_name = "car_detail.html"


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarUpdateView(UpdateView):
    """
    Atualiza um carro
    """

    model = Car
    form_class = CarModelForm
    template_name = "car_update.html"

    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarDeleteView(DeleteView):
    model = Car
    template_name = "car_delete.html"
    success_url = reverse_lazy("cars_list")

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Funcionario


class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    success_url = reverse_lazy('funcionario_list')


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionario_list')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    success_url = reverse_lazy('funcionario_list')

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)
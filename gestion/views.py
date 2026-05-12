from django.shortcuts import render, redirect, get_object_or_404

from .models import Cliente, Empleado, Mesa, Plato, Orden, Factura
from .forms import (
    ClienteForm,
    EmpleadoForm,
    MesaForm,
    PlatoForm,
    OrdenForm,
    FacturaForm,
)


def inicio(request):
    context = {
        'total_clientes': Cliente.objects.count(),
        'total_empleados': Empleado.objects.count(),
        'total_mesas': Mesa.objects.count(),
        'total_platos': Plato.objects.count(),
        'total_ordenes': Orden.objects.count(),
        'total_facturas': Factura.objects.count(),
    }
    return render(request, 'gestion/inicio.html', context)


# --- Cliente ---
def cliente_lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion/cliente_lista.html', {'clientes': clientes})


def cliente_crear(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_lista')
    else:
        form = ClienteForm()
    return render(request, 'gestion/cliente_form.html', {'form': form, 'titulo': 'Crear cliente'})


def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_lista')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'gestion/cliente_form.html', {'form': form, 'titulo': 'Editar cliente', 'cliente': cliente})


def cliente_eliminar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_lista')
    return render(request, 'gestion/cliente_confirm_delete.html', {'cliente': cliente})


# --- Empleado ---
def empleado_lista(request):
    empleados = Empleado.objects.all()
    return render(request, 'gestion/empleado_lista.html', {'empleados': empleados})


def empleado_crear(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado_lista')
    else:
        form = EmpleadoForm()
    return render(request, 'gestion/empleado_form.html', {'form': form, 'titulo': 'Crear empleado'})


def empleado_editar(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado_lista')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'gestion/empleado_form.html', {'form': form, 'titulo': 'Editar empleado', 'empleado': empleado})


def empleado_eliminar(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado_lista')
    return render(request, 'gestion/empleado_confirm_delete.html', {'empleado': empleado})


# --- Mesa ---
def mesa_lista(request):
    mesas = Mesa.objects.all()
    return render(request, 'gestion/mesa_lista.html', {'mesas': mesas})


def mesa_crear(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mesa_lista')
    else:
        form = MesaForm()
    return render(request, 'gestion/mesa_form.html', {'form': form, 'titulo': 'Crear mesa'})


def mesa_editar(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect('mesa_lista')
    else:
        form = MesaForm(instance=mesa)
    return render(request, 'gestion/mesa_form.html', {'form': form, 'titulo': 'Editar mesa', 'mesa': mesa})


def mesa_eliminar(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    if request.method == 'POST':
        mesa.delete()
        return redirect('mesa_lista')
    return render(request, 'gestion/mesa_confirm_delete.html', {'mesa': mesa})


# --- Plato ---
def plato_lista(request):
    platos = Plato.objects.all()
    return render(request, 'gestion/plato_lista.html', {'platos': platos})


def plato_crear(request):
    if request.method == 'POST':
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plato_lista')
    else:
        form = PlatoForm()
    return render(request, 'gestion/plato_form.html', {'form': form, 'titulo': 'Crear plato'})


def plato_editar(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == 'POST':
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect('plato_lista')
    else:
        form = PlatoForm(instance=plato)
    return render(request, 'gestion/plato_form.html', {'form': form, 'titulo': 'Editar plato', 'plato': plato})


def plato_eliminar(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == 'POST':
        plato.delete()
        return redirect('plato_lista')
    return render(request, 'gestion/plato_confirm_delete.html', {'plato': plato})


# --- Orden ---
def orden_lista(request):
    ordenes = Orden.objects.select_related('cliente', 'empleado', 'mesa').all()
    return render(request, 'gestion/orden_lista.html', {'ordenes': ordenes})


def orden_crear(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orden_lista')
    else:
        form = OrdenForm()
    return render(request, 'gestion/orden_form.html', {'form': form, 'titulo': 'Crear orden'})


def orden_editar(request, pk):
    orden = get_object_or_404(Orden, pk=pk)
    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('orden_lista')
    else:
        form = OrdenForm(instance=orden)
    return render(request, 'gestion/orden_form.html', {'form': form, 'titulo': 'Editar orden', 'orden': orden})


def orden_eliminar(request, pk):
    orden = get_object_or_404(Orden, pk=pk)
    if request.method == 'POST':
        orden.delete()
        return redirect('orden_lista')
    return render(request, 'gestion/orden_confirm_delete.html', {'orden': orden})


# --- Factura ---
def factura_lista(request):
    facturas = Factura.objects.select_related('orden').all()
    return render(request, 'gestion/factura_lista.html', {'facturas': facturas})


def factura_crear(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('factura_lista')
    else:
        form = FacturaForm()
    return render(request, 'gestion/factura_form.html', {'form': form, 'titulo': 'Crear factura'})


def factura_editar(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('factura_lista')
    else:
        form = FacturaForm(instance=factura)
    return render(request, 'gestion/factura_form.html', {'form': form, 'titulo': 'Editar factura', 'factura': factura})


def factura_eliminar(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if request.method == 'POST':
        factura.delete()
        return redirect('factura_lista')
    return render(request, 'gestion/factura_confirm_delete.html', {'factura': factura})

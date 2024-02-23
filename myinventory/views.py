from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import InventoryItem

def add_inventory(request):
    if request.method == 'POST':
        product_name = request.POST.get('item_name')
        quantity = int(request.POST.get('quantity'))
        vendor = request.POST.get('vendor')
        mrp = request.POST.get('mrp')
        batch_num = request.POST.get('batch_num')
        batch_date = request.POST.get('batch_date')
        status = request.POST.get('status')
        InventoryItem.objects.create(product_name=product_name, quantity=quantity,vendor=vendor,batch_num=batch_num,
                                    mrp=mrp,batch_date=batch_date,status=status)
        msg = "Inventory item added successfully"
        return render(request, "add_inventory.html",{'msg':msg})
        # return HttpResponse("Inventory item added successfully")
    else:
        return render(request, 'add_inventory.html')

def change_inventory(request, item_id):
    item = get_object_or_404(InventoryItem, pk=item_id)
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        quantity = int(request.POST.get('quantity'))
        mrp = float(request.POST.get('mrp'))
        vendor = request.POST.get('vendor')
        batch_num = request.POST.get('batch_num')
        batch_date = request.POST.get('batch_date')
        status = request.POST.get('status')

        item.product_name = product_name
        item.quantity = quantity
        item.mrp = mrp
        item.vendor =vendor
        item.batch_num = batch_num
        item.batch_date = batch_date
        item.status = status
        item.save()
        print('---------',item)
        return HttpResponse("Inventory item updated successfully")
    else:
        return render(request, 'change_inventory.html', {'item': item})

def remove_inventory(request, item_id):
    item = get_object_or_404(InventoryItem, pk=item_id)
    item.delete()
    return HttpResponse("Inventory item deleted successfully")

def pending_inventory(request):
    pending_items = InventoryItem.objects.filter(status='pending')
    return render(request, 'pending_inventory.html', {'pending_items': pending_items})

def approve_inventory_item(request, item_id):
    item = get_object_or_404(InventoryItem, pk=item_id)
    item.is_approved = True
    item.save()
    return HttpResponse("Inventory item approved successfully")


# <a href="{% url 'approve_inventory_item' item.id %}">Approve</a> 
# <form method="post" action="{% url 'remove_inventory' item.id %}">
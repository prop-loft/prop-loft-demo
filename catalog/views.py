from django.shortcuts import render

from .models import Item


def item_list(request):
    query = request.GET.get("q", "").strip()
    items = Item.objects.select_related("bin")
    if query:
        items = items.filter(name__icontains=query)
    return render(request, "catalog/item_list.html", {"items": items, "query": query})

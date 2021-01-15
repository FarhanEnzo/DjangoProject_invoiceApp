from django.shortcuts import render
from invoice_app.models import Item_entry, Item_sold
from invoice_app import forms  # (to connect with from.py classes)



def base(request):
    diction= {}

    return render(request, 'invoice_app/base.html', context=diction )


def home(request):

    diction = {"home_text" : "Welcome to Food'oice"}

    return render(request, 'invoice_app/home.html', context=diction )

def index(request):

    food_list = Item_entry.objects.order_by("item_name")

    diction = {"text1": "List of food items", "food_list": food_list}
    return render(request, 'invoice_app/index.html', context=diction)


def form(request):

    new_form = forms.EntryForm()  # creating a ItemEnrty_Form object 

    if request.method == 'POST':   #  to cheack wheather the has submitted or not 

        # if condition supports,the submitted form will override in new_form   
        new_form = forms.EntryForm(request.POST) 

        if new_form.is_valid():   #cheaking validations
            new_form.save(commit="True") # to save information in models

            return index(request) # to view the update in index page
    else:
        diction= {"item_form": new_form, "heading_1" : "Add new items"}
        return render(request, 'invoice_app/form.html', context=diction)




def orderForm(request):

    form = forms.OrderForm()

    if request.method == "POST":

        form = forms.OrderForm(request.POST)

        if form.is_valid():
            form.save(commit="True")

            return index(request)

    diction = {"title": "place an order", "order_form": form}

    return render(request, 'invoice_app/orderForm.html', context=diction)

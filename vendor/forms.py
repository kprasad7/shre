from django.forms import ModelForm

from details.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['company_name', 'branch', 'position', 'other_costs', 'salary' , 'category' , 'vendor', 'slug','description','project_cost', 'image','thumbnail']
        

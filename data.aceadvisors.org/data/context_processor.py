from .models import Indicator

def get_indicators(request):
    return  {
        "all_indicators": Indicator.objects.all()
    }
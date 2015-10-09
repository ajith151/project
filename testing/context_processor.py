import random
from .models import article

def all_objects(request):
	total = article.objects.all()	
	cn = random.sample(total,3)
	rows = {'test1':cn}
	return rows

''' this function all_objects returns 3 random values which are used in template 'whereto.html'. 
	these values are then processed to obtain the values of view 'article'.
	context_processor.py is been registered in settings.py hence, function all_objects acts as 
	a global function which can be accessed in any templates used.'''
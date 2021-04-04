customers = Customer.objects.all()
#retorna todos las personas de la tabla Persona

firsCustomer = Customer.objects.first()
# #retorna la primera persona en la tabla

lastCustomer = Customer.objects.last()
# #retorna la ultima persona en la tabla

customerById = Customer.objects.get(nombre="Carolina")
# #retorna solo la persona que se busca con ese nombre

firsCustomer.order_set.all()

products = Product.filter(numeroFicha="12345"))
# #retorna los generos con el numero de ficha relacionado 

leastToGreatest = Product.objects.all().order_by('id')
# print(personas)
# #ordena segun id
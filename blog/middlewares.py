from .models import IPaddress

class SaveIPAddressMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response


	def __call__(self, request):


		x_forward_for = request.META.get('HTTP_X_FORWARD_FOR')
		print(x_forward_for)
		if x_forward_for:
			ip = x_forward_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')

		
		try:
			ip_address = IPaddress.objects.get(ip=ip)
		except IPaddress.DoesNotExist:
			ip_address = IPaddress(ip=ip)
			ip_address.save()

		request.user.ip_address = ip_address
		
		response = self.get_response(request)



		return response

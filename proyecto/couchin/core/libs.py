def check_temporal(user):
	try:
		res = user.temp_pass
	except Exception:
		res = False

	return not res

def check_admin(user):
	return user.admin
from statusTracking.models import AuthUser, AuthUserGroups,AuthGroup

class Employee:
	def __init__(self, name):
		pc = AuthGroup.objects.get(name="PC")
		cr = AuthGroup.objects.get(name="CR")
		cv = AuthGroup.objects.get(name="CV")
		pt = AuthGroup.objects.get(name="PT")
		wh = AuthGroup.objects.get(name="WH")
		gm = AuthGroup.objects.get(name="GM")
		user = AuthUser.objects.get(username=name)
		
		self.username = name
		self.id = user.id
		self.firstname = user.first_name
		self.lastname = user.last_name
#		self.task = AuthUserGroups.objects.filter(user_id = self.id, group_id = cr.id).count()
		if (AuthUserGroups.objects.filter(user_id = self.id, group_id = pc.id).count() > 0):
			self.task = "PC"
		elif (AuthUserGroups.objects.filter(user_id = self.id, group_id = cr.id).count() > 0):
			self.task = "CR"
		elif (AuthUserGroups.objects.filter(user_id = self.id, group_id = cv.id).count() > 0):
			self.task = "CV"
		elif (AuthUserGroups.objects.filter(user_id = self.id, group_id = pt.id).count() > 0):
			self.task = "PT"
		elif (AuthUserGroups.objects.filter(user_id = self.id, group_id = wh.id).count() > 0):
			self.task = "WH"
		elif (AuthUserGroups.objects.filter(user_id = self.id, group_id = gm.id).count() > 0):
			self.task = "GM"


from django.db.models import (
Model, ForeignKey, CASCADE,

)
class Account(Model):
	pass
	
	
class AssetLifecycle(Model):
	class Status():
		ACQUIRED = "ACQ", _('Asset Purchase / Not In Use')
		IN_USE = "USE",_('Current Asset / In Use')
		DISPOSED = "DEL",_('Asset Disposed of')
	lifecycle_name
	lifecycle_description
	lifecycle_status
	
class Asset(Model):
	lifecycle = ForeignKey(AssetLifecycle, on_delete=CASCADE)


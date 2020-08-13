class Attachment:
	class Category:
		CONTACT_PHOTO = "ADDR"
		DOCUMENT = "DOC"
		Image = "IMG"
		RECEIPT = "RCT"
		SIGNATURE = "SIG"
		SOUND = "AUD"
		OTHER = "OTH"
	class AttachableReference:
		# thing about status
		ACTIVE = 1
		INACTIVE = 0

    SyncToken: 0, 
    domain: QBO, 
    AttachableRef: [
      {
        IncludeOnSend: false, 
        EntityRef: {
          type: Invoice, 
          value: 95
        }
      }
    ], 
    Note: This is an attached note., 
    sparse: false, 
    Id: 200900000000000008541, 
    MetaData: {
      CreateTime: 2015-11-17T11:05:15-08:00, 
      LastUpdatedTime: 2015-11-17T11:05:15-08:00
    }
  }, 
  time: 2015-11-17T11:05:15.797-08:00
}

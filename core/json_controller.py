import json
from pathlib import Path
		
class JSONController:
	@staticmethod	
		def open_init_data_json():
		BASE_DIR = Path.cwd() 
		FILE_PATH = BASE_DIR /"statements" /"init_data"/"multi_step_income_statement_data.json"
		with open(FILE_PATH) as json_file:
			data = json.load(json_file)
			return data
	@staticmethod
	def save_json():
		pass

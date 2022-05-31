from tinydb import TinyDB, Query
import global_variables

class UserMgmt:

	def __add_dummies__(self):
		
		Speaker = Query()
		if (not self.speaker_table.contains(Speaker.name == 'Sera')):
			self.speaker_table.insert({"name": "sera", "language": "de", "gender": "male", "voice": [3.496027, 2.742538, 7.009655, 1.345091, 3.557887, 1.985651, 3.878922, 3.306595, 0.521702, -0.933573, 5.831099, 1.063725, 6.220464, 0.253629, 1.276216, 0.143699, 4.492473, 3.085272, 4.890385, 6.44916, 1.302725, -1.123645, 6.820951, 2.89459, 3.301397, 0.469813, 4.166016, 7.263201, 3.949481, 6.750736, 3.987867, -0.106461, 1.126318, 3.017034, 2.665097, -0.304168, 2.093874, 0.755348, 4.575878, 3.744673, 1.917072, 2.594373, 2.190459, 3.569955, 3.123753, -0.795704, 1.346052, 3.961041, 2.873615, 3.991129, 4.252429, 3.299643, 2.048348, 4.908381, 0.171587, 1.007092, 3.666463, 0.617667, 2.98171, 4.717092, 0.074256, 0.559496, 3.67191, 3.805041, 3.811503, 0.360366, 4.812425, 1.300776, 0.641981, 2.884212, 6.398939, -0.35681, 3.245203, 1.292347, 3.206867, 4.668324, 3.386766, 5.135428, 4.426035, 4.411294, 5.138068, 2.139814, 2.365171, 4.231797, 3.869509, -0.231328, 3.367212, 1.128239, 4.391038, 4.726377, 0.273992, 2.42836, 1.316217, 4.772497, 6.345689, 1.624428, 3.308609, 0.108634, 4.322318, 1.953723, 2.401819, 2.392952, 0.329102, 4.137652, 1.818093, 3.918409, 0.474253, 3.184205, -0.886284, 3.802032, 2.91726, 1.163475, 3.371105, -0.196885, 3.433325, 3.232873, 3.727185, 3.799502, 6.640769, 2.729447, 0.246235, 8.005991, 5.375033, 0.46788, 0.513793, 0.435058, 4.855752, -0.588781],'phone':'4915148976452'})
	
		if (not self.speaker_table.contains(Speaker.name == 'sarah')):
			self.speaker_table.insert({'name': 'sarah', 'gender': 'female', 'voice': [6.568451, 6.784739, 5.919335, -0.037495, 5.012778, 3.429874, 0.197787, 4.527809, 4.255286, -2.130709, 5.589361, -3.622524, 4.508074, 3.356104, 3.682185, 0.044928, 0.479103, 2.203794, 3.632379, 3.791435, -0.37931, 1.265373, 6.435224, 4.998378, 1.799174, 0.382703, 3.253555, 7.215866, 5.043785, 2.663403, 7.665906, -3.570974, 1.6675, 4.020483, -4.763138, 3.499512, 1.714248, -0.560638, 4.49633, 1.303618, -6.767202, 2.607261, 2.53354, 3.470852, 5.046845, 0.081558, -0.458351, 6.547997, 4.702069, 1.162, 7.732637, 4.443409, 2.84802, 3.515044, 1.404639, -2.716206, 7.028213, -0.252494, 0.31498, 2.893929, -3.77118, 1.205617, 1.795407, 4.893912, 0.521469, -4.615733, 2.547347, -1.403257, 2.687941, 3.193995, 5.99359, 1.825902, 1.973971, 2.642833, 4.234736, 1.145308, -0.519826, 7.352092, 1.77186, 1.947172, 6.951781, 2.769729, 4.519409, 8.090642, 3.032326, 2.692257, 0.98964, -4.389252, 5.47305, 3.880094, -3.5125, 1.346476, 1.295684, 8.435177, 4.487869, 1.237189, 3.073678, -5.445618, 5.607491, 6.903141, 0.258461, 4.483095, 6.992905, 3.336628, 5.016744, 3.078014, 2.637331, 2.047266, 2.220054, 3.3177, 4.209452, -3.704949, 5.010245, -4.430152, -1.731702, 3.403976, 6.573786, 1.421829, 5.792188, 1.567448, 0.59064, 4.689801, 3.367578, 2.579401, -6.780087, -1.828632, 4.636183, 0.699218], 'phone':'4915208768386'})		

	def __init__(self, init_dummies=False):
		self.db = TinyDB('./users.json')
		self.speaker_table = self.db.table('speakers')
		if init_dummies:
			self.__add_dummies__()
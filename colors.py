class Colors:
	dark_grey = (26, 31, 40)
	green = (23, 230, 47)
	red = (232, 18, 18)
	orange = (216, 116, 18)
	yellow = (237, 234, 10)
	cyan = (21, 203, 208)
	purple = (166, 0, 247)
	blue = (13, 64, 216)
	light = (255,255,255)
	dark_blue = (44, 44, 127)
	light_blue = (59, 85, 162)

	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.green, cls.red,cls.orange, cls.yellow, cls.cyan, cls.purple, cls.blue]

	@classmethod
	def set_custom_colors(cls, custom_colors):
		if len(custom_colors) == len(Colors.get_cell_colors()):
			for	i in range(len(custom_colors)):
				cls.get_cell_colors()[i] = custom_colors[i]
		else:
			print("Custom colors must match the number of default colors.")

	def choose_custom_colors(self):
		custom_colors = []
		for i in range(len(Colors.get_cell_colors())):
			color_str = input(f"Enter color for cell {i+1} as (R, G, B): ")
			color = tuple(map(int, color_str.split(',')))
			custom_colors.append(color)
		return custom_colors


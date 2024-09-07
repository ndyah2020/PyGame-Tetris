import pygame
from colors import Colors
class Grid:
	def __init__(self):
		self.landing_sound = pygame.mixer.Sound('sound/break.mp3')
		self.landing_sound.set_volume(0.3)
		self.num_rows = 20
		self.num_cols = 10
		self.cell_size = 30
		self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
		self.colors = Colors.get_cell_colors()

	#In lưới 
	def print_grid(self):
		for row in range(self.num_rows):
			for col in range(self.num_cols):
				print(self.grid[row][col], end = " ")
			print()

	#Kiểm tra xem khối có trong lưới hay không? 
	def is_inside(self, row, col):
		if row >=0 and row < self.num_rows and col >= 0 and col < self.num_cols:
			return True
		return False

	#Kiểm tra xem ô có trống không?
	def is_empty(self, row, col):
		if self.grid[row][col] == 0:
			return True
		return False

	#Kiểm tra xem hàng đã lắp đầy chưa 
	def is_row_full(self, row):
		for col in range(self.num_cols):
			if self.grid[row][col] == 0:
				return False
		return True

	#Xóa hàng 
	def clear_row(self, row):
		for col in range(self.num_cols):
			self.landing_sound.play()
			self.grid[row][col] = 0

	#Di chuyển 1 hàng xuống theo số hàng quy định 
	def move_row_down(self, row, num_rows):
		for col in range(self.num_cols):
			self.grid[row + num_rows][col] = self.grid[row][col]
			self.grid[row][col] = 0

	#Xóa completed hàng đã lắp đầy và di chuyển xuống cuối lưới 
	def clear_full_rows(self):
		completed = 0
		for row in range(self.num_rows-1, 0, -1):
			if self.is_row_full(row):
				self.clear_row(row)
				completed +=1 
			elif completed > 0:
				self.move_row_down(row, completed)
		return completed


	def draw(self, screen):
		for row in range(self.num_rows):
			for col in range(self.num_cols):
				cell_value = self.grid[row][col]	
				cell_rect = pygame.Rect(col*self.cell_size + 11, row*self.cell_size + 11, 
				self.cell_size - 1, self.cell_size - 1)
				pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

	def reset(self):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				self.grid[row][column] = 0		






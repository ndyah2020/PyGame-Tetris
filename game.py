from grid import Grid
from blocks import *
import random
import pygame

class Game:
	def __init__(self):
		self.grid = Grid()
		self.blocks = [IBlock(),JBlock(),LBlock(),
		OBlock(),SBlock(),TBlock(),ZBlock()]
		self.current_block=self.get_random_block()
		self.next_block =self.get_random_block()
		self.game_over = False
		self.score = 0
		self.break_sound = pygame.mixer.Sound('sound/break.mp3')
		self.break_sound.set_volume(0.7)

	#Cập nhật điểm số(số hàng được lắp đầy , số điểm)
	def update_score(self, line_cleared, move_down_points):
		if line_cleared == 1:
			self.score+=100
		elif line_cleared == 2:
			self.score+=300
		elif line_cleared == 3:
			self.score+=500
		self.score += move_down_points

	#Lấy ngẫu nhiên 1 
	def get_random_block(self):
		if len(self.blocks) == 0:
			self.blocks = [IBlock(),JBlock(),LBlock(),
		OBlock(),SBlock(),TBlock(),ZBlock()]
		block = random.choice(self.blocks)
		self.blocks.remove(block)
		return block

	#Di chuyển khối qua trái
	def move_left(self):
		self.current_block.move(0,-1)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, 1)

	#Di chuyển khối qua phải 
	def move_right(self):
		self.current_block.move(0, 1)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, -1)

	#Di chuyển khối xuống dưới 
	def move_down(self):
		self.current_block.move(1, 0)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(-1, 0)
			self.lock_block()

	def drop(self) :
		self.break_sound.play()
		while self.block_inside() and self.block_fits():
			self.current_block.move(1, 0)
		self.current_block.move(-1, 0)
		self.lock_block()

	def lock_block(self):
		tiles = self.current_block.get_cell_position()
		for position in tiles:
			self.grid.grid[position.row][position.col] = self.current_block.id
		self.update_score(0, 4)
		self.current_block = self.next_block
		self.next_block = self.get_random_block()
		rows_cleared = self.grid.clear_full_rows()
		if rows_cleared > 0:
			self.update_score(rows_cleared, 0)	
		if self.block_fits() == False:
			self.game_over = True

	#Kiểm tra xem có thể đặt khối mới hay không 
	def block_fits(self):
		tiles = self.current_block.get_cell_position()
		for tile in tiles:
			if self.grid.is_empty(tile.row, tile.col) == False:
				return False
		return True

	#Kiểm tra khối có nằm trong lưới không? 
	def block_inside(self):
		tiles = self.current_block.get_cell_position()
		for tile in tiles:
			if self.grid.is_inside(tile.row, tile.col) == False:
				return False
		return True

	#Kiểm tra xoay khối 
	def rotate(self):
		self.current_block.rotate()
		if self.block_inside() == False or self.block_fits() == False :
			self.current_block.undo_rotate()


	def draw(self, screen):
		self.grid.draw(screen)
		self.current_block.draw(screen, 11, 11)
		if self.next_block.id == 3:
			self.next_block.draw(screen, 253, 275)
		elif self.next_block.id == 4:
			self.next_block.draw(screen, 253, 268)
		elif self.next_block.id == 5 or  self.next_block.id == 2:
			self.next_block.draw(screen, 270, 260)
		else:
			self.next_block.draw(screen, 245, 260)

	def reset(self):
		self.grid.reset()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.score = 0
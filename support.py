import pygame
from csv import reader
from settings import tile_size
from os import walk

def import_folder(path):
	# create an empty list 
	surface_list = []
	# check files in directory
	for _, __, image_files in walk(path):
		for image in image_files:
			# for every file in  directory create a full path to that file
			full_path = path + '/' + image
			# create a surface from that image in the directory
			image_surf = pygame.image.load(full_path).convert_alpha()
			# append that image to the list and return list
			surface_list.append(image_surf)
	# func creates a list of surfaces with certain images
	return surface_list

def import_csv_layout(path):
	# create an empty list
	terrain_map = []
	# open a csv file which contains numbers from -1 to 9
	with open(path) as map:
		# read the data
		level = reader(map, delimiter = ',')
		# take every row(they all have equal lenght) and add it to the list
		for row in level:
			terrain_map.append(list(row))
		# func creates list of lists
		# there a 11 lists in the main list which correlate with vertical tile number
		# in every inner list there are numbers from -1 to 9 that defines what image there will be 
		return terrain_map

def import_cut_graphics(path):
	# load a whole image as surface from directory
	surface = pygame.image.load(path).convert_alpha()
	# define how many tiles we get from that image
	tile_num_x = int(surface.get_size()[0] / tile_size)
	tile_num_y = int(surface.get_size()[1] / tile_size)
	# create empty list for new tiles
	cut_tiles = []
	for row in range(tile_num_y):
		for col in range(tile_num_x):
			# we get certain part of image and get only a little tile with coordinates x, y
			x = col * tile_size
			y = row * tile_size
			new_surf = pygame.Surface((tile_size, tile_size), flags = pygame.SRCALPHA)
			new_surf.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
			cut_tiles.append(new_surf)
	# func creates a list with tiles 
	return cut_tiles

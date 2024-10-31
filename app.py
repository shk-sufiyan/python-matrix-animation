import os, random, sys, time

class MatrixAnimation():

	## set dimension
	COLUMN = 80
	ROW = 24

	## characters option
	CHARS = ["0", "1", " ", " ", "0", " ", " ", " "]

	def __init__(self):

		matrix = self.generate_matrix()

		## now animate the matrix
		self.animate(matrix)


	## animate the matrix
	def animate(self, matrix):
		try:
			while True:
				self.update_effect(matrix)
				self.generate_effect(matrix)
				time.sleep(0.1)
		except KeyboardInterrupt as e:
			print("Good bye!!!")


	## update the matrix
	def update_effect(self, matrix):
		for a_column in range(self.COLUMN):
			if random.random() > 0.85:
				matrix[a_column] = random.choice(self.CHARS)

	## generate the matrix effect
	def generate_effect(self, matrix):
		# self.clear_animation()

		for a_row in range(self.ROW):
			for a_column in range(self.COLUMN):

				a_char = matrix[a_column] if a_row < random.randint(1, self.ROW) else " "
				print(f"\033[92m{a_char}\033[0m", end="")

			print()

	## generate the random matrix chars
	def generate_matrix(self):
		matrix = [random.choice(self.CHARS) for _ in range(self.COLUMN)]
		return matrix

	## close the animation on termination
	def clear_animation(self):
		os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == '__main__':
	MatrixAnimation()
##---------------------------------------------------------------------
#	Confusion_Matrix
#	Construction:	input the class number of dataset
#	zero_mat:		Set the Confusion_Matrix to zero
#	static_a_batch: Static the Confusion_Matrix of current batch
#	normalize:		Divided by the sum
#	show_mat:		print the matrix in cmd
##---------------------------------------------------------------------

import torch
import torch.nn as nn
import numpy as np
class Confusion_Matrix(object):
	def __init__(self, dim):
		self.dim = dim
		self.con_mat = torch.zeros(dim, dim)
	
	def zero_mat(self):
		self.con_mat *= 0

	def static_a_batch(self, predict, groundtruth):
		# batch_size = predict.size(0)
		#batch_size = 1
		#for i in range(batch_size):
	        self.con_mat[int(groundtruth),int(predict)] += 1

	def normalize(self):
		sum_m = torch.sum(self.con_mat,1)
		for i in range(sum_m.size(0)):
			self.con_mat[i,:]= self.con_mat[i,:]/sum_m[i]

	def show_mat(self):
		np.save("loca-r1.npy",self.con_mat)

		print(self.con_mat.diag())
                
	def get_mat(self):
		return self.con_mat

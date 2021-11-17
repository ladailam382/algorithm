class Node:
	def __init__(self,k,p,left=None,right=None):
		self.id = k
		self.priority = p
		self.leftchild = left
		self.rightchild = right


class Mytree:
	def __init__(self):
		self.root = None

	def right_rotate(self,a):
		b = a.leftchild
		a.leftchild = b.rightchild
		b.rightchild = a
		return b

	def left_rotate(self,a):
		b = a.rightchild
		a.rightchild = b.leftchild
		b.leftchild = a
		return b

	def insert(self,start,k,p):
		if start is None:
			return Node(k,p)
		if k<start.id:
			start.leftchild = self.insert(start.leftchild,k,p)
			if start.priority < start.leftchild.priority:
				start = self.right_rotate(start)
		else:
			start.rightchild = self.insert(start.rightchild,k,p)
			if start.priority < start.rightchild.priority:
				start = self.left_rotate(start)
		return start

	def real_insert(self,k,p):
		self.root = self.insert(self.root,k,p)

	def find(self,start,k):
		if start.id == k:
			return 'yes'
		if start.id > k:
			if start.leftchild is None:
				return 'no'
			else:
				return self.find(start.leftchild,k)
		else:
			if start.rightchild is None:
				return 'no'
			else:
				return self.find(start.rightchild,k)

	def print_tree_preorder(self,start):
		l = " "+self.print_tree_preorder(start.leftchild) if start.leftchild is not None else ''
		r = ' '+self.print_tree_preorder(start.rightchild) if start.rightchild is not None else ''
		return str(start.id) + l + r

	def print_tree_inorder(self,start):
		l = self.print_tree_inorder(start.leftchild)+' ' if start.leftchild is not None else ''
		r = ' ' + self.print_tree_inorder(start.rightchild) if start.rightchild is not None else ''
		return l + str(start.id) + r

	def _delete(self,start,k):

		if start is None:
			return None
		elif start.id < k:
			start.rightchild = self._delete(start.rightchild, k)
		elif start.id > k:
			start.leftchild = self._delete(start.leftchild, k)
		else:
			if start.leftchild is None and start.rightchild is None:
				return None
			elif start.rightchild is None:
				start = self.right_rotate(start)

			elif start.leftchild is None:
				start = self.left_rotate(start)
			else:
				if start.leftchild.priority > start.rightchild.priority:
					start = self.right_rotate(start)
				else:
					start = self.left_rotate(start)

			return self._delete(start,k)
		return start

	def real_delete(self,k):
		self.root = self._delete(self.root,k)

n = int(input())
LL = Mytree()
for _ in range(n):
	x = input().split()
	x[1:] = list(map(int,x[1:]))
	if x[0] == 'insert':
		LL.real_insert(int(x[1]),x[2])
	elif x[0] == 'find':
		print(LL.find(LL.root,x[1]))
	elif x[0] == 'print':
		print(' '+LL.print_tree_inorder(LL.root))
		print(' '+LL.print_tree_preorder(LL.root))
	else:
		LL.real_delete(x[1])

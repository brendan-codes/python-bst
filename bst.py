class BST:
	def __init__(self):
		self.root = None
		self.count = 0

	def add(self, val, current=None):
		if not self.root:
			self.root = BSNode(val)
			self.count += 1
			return self
		
		if not current:
			current = self.root

		if val == current.val:
			current.dupes += 1
			return self

		if val > current.val:
			if not current.right:
				current.right = BSNode(val)
				self.count += 1
				return self
			else:
				self.add(val, current.right)

		if val < current.val:
			if not current.left:
				current.left = BSNode(val)
				self.count += 1
				return self
			else:
				self.add(val, current.left)

		return self

	def isValid(self):
		if not self.root:
			return True
		else:
			result = self.root.isValid()
			if result == None:
				return True
			else:
				return result
			






	def print(self):
		if self.root:
			self.root.traverse()

	def getHeight(self):
		if self.root:
			return self.root.height()



class BSNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.dupes = 0

	def isValid(self, leftm=None, rightm=None):
		if not leftm:
			leftm = self.val - 1

		if not rightm:
			rightm = self.val

		print(leftm)
		print(rightm)

		if self.left:
			if self.left.val > leftm:
				return False
			else:
				return self.left.isValid(self.left.val - 1, self.left.val)

		if self.right:
			if self.right.val < rightm:
				return False
			else:
				return self.right.isValid(self.right.val - 1, self.right.val)



	def traverse(self):
		print(self.val)
		if self.left:
			self.left.traverse()
		if self.right:
			self.right.traverse()

	def height(self):
		l, r = 0, 0
		if not self.right and not self.left:
			return 1
		if self.right:
			r = self.right.height()
		if self.left:
			l = self.left.height()

		if l >= r:
			return l + 1
		else:
			return r + 1


treefiddy = BST()
treefiddy.add(50)
treefiddy.add(75)
treefiddy.add(66)
treefiddy.add(25)
treefiddy.add(33)

# treefiddy.add(26)

# treefiddy.print()
# print(treefiddy.getHeight())
print(treefiddy.isValid())

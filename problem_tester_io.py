import sys
import os
import subprocess
import shutil

def cmp(p1, p2) -> bool:
	f1 = open(p1, 'r')
	f2 = open(p2, 'r')

	l1 = f1.read().split('\n')
	l2 = f2.read().split('\n')

	if l1[-1] == '':
		l1.pop()

	if l2[-1] == '':
		l2.pop()
	
	if len(l1) != len(l2):
		return False
	
	for i in range(len(l1)):
		if l1[i] != l2[i]:
			return False
	
	return True


problem_name: str
if len(sys.argv) > 1:
	problem_name = sys.argv[1]
else:
	problem_name = input()

print(os.getcwd())
problem_path = os.path.join(os.getcwd(), 'problems', problem_name)
print(problem_path)

inputPath = lambda n: os.path.join(problem_path, 'in', f'input{str(n)}.txt')
outputPath = lambda n: os.path.join(problem_path, 'out', f'output{str(n)}.txt')
soloutPath = lambda n: os.path.join(problem_path, 'slo', f'output{str(n)}.txt')
solutionPath = os.path.join(problem_path, 'solution.py')

try:
	shutil.rmtree(os.path.join(problem_path, 'slo'))
except:
	pass

# Make Solution Output directory
os.mkdir(os.path.join(problem_path, 'slo'))

err = False

for i in range(1, 51):
	run = subprocess.run(
		args=[
			os.path.join('venv', 'bin', 'python'),
			solutionPath
		],
		stdin=open(inputPath(i), 'r'),
		stdout=open(soloutPath(i), 'w+')
	)

	if not cmp(outputPath(i), soloutPath(i)):
		print('Wrong answer')
		err = True
		break


if err:
	raise Exception("Failed Wrong at", i)
else:
	# Remove Solution Output directory
	shutil.rmtree(os.path.join(problem_path, 'slo'))
	print('All OK!')
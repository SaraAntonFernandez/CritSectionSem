from multiprocessing import Process, current_process, Value, Array, Lock

N=8

def task(common, tid, lock):
	a=0
	for i in range(100):
		print (f"{tid}−{i}: Non−critical Section")
		a+=1
		print (f"{tid}−{i}: End of non-critical Section")
		lock.acquire()
		try:
			print (f"{tid}−{i}: Critical Section")
			v = common.value +1
			print (f"{tid}−{i}: Inside critical Section")
			common.value=v
			print (f"{tid}−{i}: End of critical Section")
		finally:
			lock.release()

def main():
	lp=[]
	common=Value('i',0)
	lock=Lock()
	for tid in range(N):
		lp.append(Process(target=task, args=(common, tid, lock)))
	for p in lp:
		p.start()
	for p in lp:
		p.join()
	print (f"Valor final del contador {common.value}")
	print ("fin")

if __name__=="__main__":
	main()

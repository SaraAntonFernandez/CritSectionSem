from multiprocessing import Process, current_process, Value, Array, BoundedSemaphore

N=8
k=4

def task(common, tid, semaforo):
	a=0
	for i in range(100):
		print (f"{tid}−{i}: Non−critical Section")
		a+=1
		print (f"{tid}−{i}: End of non-critical Section")
		semaforo.acquire()
		try:
			print (f"{tid}−{i}: Critical Section")
			v = common.value +1
			print (f"{tid}−{i}: Inside critical Section")
			common.value=v
			print (f"{tid}−{i}: End of critical Section")
		finally:
			semaforo.release()

def main():
	lp=[]
	common=Value('i',0)
	semaforo=BoundedSemaphore(k)
	for tid in range(N):
		lp.append(Process(target=task, args=(common, tid, semaforo)))
	for p in lp:
		p.start()
	for p in lp:
		p.join()
	print (f"Valor final del contador {common.value}")
	print ("fin")

if __name__=="__main__":
	main()

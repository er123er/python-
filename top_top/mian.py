import Bisque_free_fiction
import free_fiction
import wu5200free_fiction
from concurrent.futures import ThreadPoolExecutor
if __name__ == '__main__':
	with ThreadPoolExecutor() as t:
		t.submit(Bisque_free_fiction.main__bqg,)
		t.submit(free_fiction.main_free,)
		t.submit(wu5200free_fiction.mian_5200,)

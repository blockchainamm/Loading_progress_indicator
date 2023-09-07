from progress.bar import Bar
import time

bar = Bar('Processing', max=30)
for i in range(30):
    time.sleep(0.1)
    bar.next()
bar.finish()
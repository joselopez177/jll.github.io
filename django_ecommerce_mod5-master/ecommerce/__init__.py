import portalocker

with open('file.txt', 'w') as file:
    portalocker.lock(file, portalocker.LOCK_EX)
    file.write('Data')
    portalocker.unlock(file)
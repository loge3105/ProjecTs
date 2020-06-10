import eel
import core

eel.init('web')

@eel.expose
def ans(a):
	eel.result(core.thickness(int(a)))

eel.start('index.html', size=(800,900))

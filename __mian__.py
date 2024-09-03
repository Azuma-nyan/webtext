import ui
import sys
import text_export as ex

path = ui.select_text()

if path == None:
  ui.stop()
  sys.exit()
  
ex.check(path)
ui.fin()
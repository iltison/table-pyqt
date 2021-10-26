готовая pyqt таблица для проектов.  
text + combobox  
# Импорт данных:  
Main([List])  
# Экспорт данных  
Main([List]).export_tv()  
  
# Встривание в MainWindow:  

  from Main import new_table_example   
  w = Main([List])  
  if w.exec_() == 0:  
      w.export_tv()  

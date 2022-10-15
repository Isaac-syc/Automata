import ast
import sys
from PyQt5 import QtWidgets, uic


class main:
   
   DFA = ""
   response = ""

   def run(self,GUI):
      
      sql = GUI.entrySql.text()
      
      
      if self.verifyDfa(self.DFA, sql):
         self.response = "La sentencia: '"+sql+"' es aceptada "
      else:
         self.response = "La sentencia: '"+sql+"' es rechazada"
      
      
      GUI.list_result.clear()
      GUI.list_result.addItem(str(self.response))

      
   def loadAutomata(self,filename):
      try:
         with open(filename, 'r', encoding='utf-8') as file:
            content = file.read() 
         DFA = ast.literal_eval(content)
         self.DFA = DFA 
         return DFA
      except Exception as e:
         print(f"Archivo no encontrado") 
   
   def verifyDfa(self,D,w):
      return self.initDfa(D,w) in D["F"]
   
   
   def initDfa(self,D,w):
      curstate = D["q0"]
      if w == "":
         return curstate
      return self.runDfaObjetct(D,w[1:], self.runDfa(D,curstate,w[0]))
   
   def runDfaObjetct(self,D,w,q):
      if w == "":
         return q
      return self.runDfaObjetct(D,w[1:], self.runDfa(D,q,w[0]))
   
   def runDfa(self,D,q,a):
      try:
         assert(a in D["Sigma"])
         assert(q in D["Q"])
         return D["Delta"][(q,a)]
      except:
         return False
     
      
if __name__ == "__main__":   
   app = QtWidgets.QApplication(sys.argv)
   GUI = uic.loadUi("interfaz.ui")
   GUI.show()
   main = main()
   
   main.loadAutomata("automata.txt")
   
   GUI.evaluate_test.clicked.connect(lambda: main.run(GUI))

   sys.exit(app.exec_())
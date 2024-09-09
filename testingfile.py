from Speechtonotes import Speechtonotes
tester=Speechtonotes()
tester.speechToText("Yes.wav")
tester.update_text()
print(tester.getNotes())




# Loading progress indicator script

This python script emulates the loading progress indicator id different forms
---

- Method 1\
  This method simulates a rotating bar next to the text loading for a given time, upon each increment of the step the symbol next to a loading text changes as shown below thereby producing a continuous rotating bar motion

   loading \ > loading - > loading | > loading /
  
  Once the process is completed the rotating bar become static after loading text and a message Done! is displayed as shown below

   <img width="62" alt="method1_completed" src="https://github.com/blockchainamm/blockchainamm/assets/82846751/a7356e41-38bc-48ab-bbdd-fbde7c5799b4">
   
---
  
- Method 2\
  This method simulates a horizontal progress bar next to the text Processing for a given time
  
  <img width="278" alt="method2_inital" src="https://github.com/blockchainamm/blockchainamm/assets/82846751/888120c2-0141-4757-92d6-760a36a36228">

  The status of the progress bar is incremented sequentially with one # character until the maximum counter limit is reached, in this case it's 30
  
  <img width="287" alt="method2_completed" src="https://github.com/blockchainamm/blockchainamm/assets/82846751/95cabe34-34a9-428a-883b-a53bafc4cd7d">

---
- Method 3\
  This method simulates a horizontal progress bar next to the text Loading until the maximum limit of 100% is reached

  Inital state
  
  <img width="93" alt="method3_inital" src="https://github.com/blockchainamm/blockchainamm/assets/82846751/6b873cc5-5e0a-4de1-ab68-a7c84129da37">
    
  Final state

  <img width="97" alt="method3_completed" src="https://github.com/blockchainamm/blockchainamm/assets/82846751/5bd822d8-8abd-41dc-a17c-8a9b889feb9f">
